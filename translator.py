# -*- coding: utf-8 -*-

import json
import os
import regex as re # Použijeme robustnější regex knihovnu

class EPLTranslator:
    """
    Třída pro překlad vět Emoji Prompt Language (EPL) srozumitelného textu.
    Verze 2.1 - Oprava parsování složených emoji a modifikátorů.
    """
    def __init__(self, grammar_map_path, emoji_db_dir):
        self.grammar_map = self._load_json(grammar_map_path)
        self.emoji_database = self._load_emoji_database(emoji_db_dir)
        if not self.emoji_database or not self.grammar_map:
            raise ValueError("Chyba při načítání potřebných JSON souborů.")

    def _load_json(self, file_path):
        if not os.path.exists(file_path):
            print(f"Chyba: Soubor '{file_path}' nebyl nalezen.")
            return None
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _load_emoji_database(self, db_dir):
        index_path = os.path.join(db_dir, "index.json")
        index = self._load_json(index_path)
        if not index or "categories" not in index:
            print(f"Chyba: Index soubor '{index_path}' je neplatný.")
            return None
        
        full_database = {}
        # print("Načítám kategorizovanou databázi emoji...") # Ztišíme pro čistší výstup
        for category_file in index["categories"]:
            emojis = self._load_json(os.path.join(db_dir, category_file))
            if emojis:
                for emoji_data in emojis:
                    full_database[emoji_data["char"]] = emoji_data
        # print(f"Úspěšně načteno {len(full_database)} emoji.")
        return full_database

    def translate(self, sentence):
        """Přeloží kompletní větu v EPL."""
        # 1. Rozdělení na tokeny (modifikátor + emoji)
        # \X je grapheme cluster, (?:(\([LS]\)))? je volitelná skupina pro modifikátor
        tokens = re.findall(r'(\([LS]\))?(\X)', sentence)
        
        if not tokens:
            return "Prázdná věta."

        # 2. Přiřazení rolí a významů
        parsed_tokens = []
        for emphasis, emoji in tokens:
            # Ignorujeme mezery a další neviditelné znaky
            if not emoji.strip():
                continue

            role = self.grammar_map.get(emoji, {}).get("role", "OBJECT")
            
            meaning = ""
            if emoji in self.grammar_map:
                meaning = self.grammar_map[emoji]["meaning"]
            elif emoji in self.emoji_database:
                meaning = self.emoji_database[emoji]["name"]
            else:
                meaning = "neznámé emoji"

            if emphasis == "(L)":
                meaning = f"důrazně {meaning}"
            elif emphasis == "(S)":
                meaning = f"méně důležitý {meaning}"

            parsed_tokens.append({"role": role, "meaning": meaning, "raw": emoji})
        
        # 3. Sestavení věty
        subject = "User"
        action = None
        objects = []
        modifiers = []
        state = None

        # Najdi subjekt
        for token in parsed_tokens:
            if token["role"] == "SUBJECT":
                subject = token["meaning"].capitalize()
                break
        
        # Najdi akci
        for token in parsed_tokens:
            if token["role"] == "ACTION":
                action = token["meaning"]
                break

        if not action:
            return f"Chyba: Věta neobsahuje žádnou akci."

        # Zbytek jsou objekty, modifikátory nebo stav
        for token in parsed_tokens:
            if token["role"] not in ["SUBJECT", "ACTION"]:
                if token["role"] == "OBJECT":
                    objects.append(token["meaning"])
                elif token["role"] == "MODIFIER":
                    modifiers.append(token["meaning"])
                elif token["role"] == "STATE":
                    state = token["meaning"]

        # 4. Formátování výstupu
        result = f"{subject} {action}"
        if objects:
            result += f" {' a '.join(objects)}"
        if modifiers:
            result += f" ({', '.join(modifiers)})"
        if state:
            result += f", stav: {state}"
        
        return result + "."

if __name__ == "__main__":
    grammar_file = "BasicEmojiLanguage/GRAMMAR_MAP.json"
    emoji_db_dir = "BasicEmojiLanguage/emoji_db"
    
    if not os.path.exists(grammar_file):
        grammar = {
            "👤": {"role": "SUBJECT", "meaning": "user"}, "🤖": {"role": "SUBJECT", "meaning": "AI"},
            "👨‍💻": {"role": "SUBJECT", "meaning": "developer"}, "🚀": {"role": "ACTION", "meaning": "starts"},
            "🔍": {"role": "ACTION", "meaning": "searches for"}, "💾": {"role": "ACTION", "meaning": "saves"},
            "⚙️": {"role": "ACTION", "meaning": "configures"}, "💬": {"role": "ACTION", "meaning": "sends message"},
            "📄": {"role": "OBJECT", "meaning": "a file"}, "🗪": {"role": "OBJECT", "meaning": "a discussion"},
            "💡": {"role": "OBJECT", "meaning": "an idea"}, "🌐": {"role": "OBJECT", "meaning": "the web"},
            "✅": {"role": "STATE", "meaning": "success"}, "❌": {"role": "STATE", "meaning": "failure"},
            "🔔": {"role": "STATE", "meaning": "notification"}, "➡️": {"role": "MODIFIER", "meaning": "then"},
            "🔄": {"role": "MODIFIER", "meaning": "in a loop"}
        }
        with open(grammar_file, 'w', encoding='utf-8') as f:
            json.dump(grammar, f, indent=4, ensure_ascii=False)

    try:
        translator = EPLTranslator(grammar_map_path=grammar_file, emoji_db_dir=emoji_db_dir)
        
        print("\n--- Test Překladače Basic Emoji Language (EPL) v2.1 (opraveno) ---\n")

        sentences = [
            "👤🚀🗪",
            "🤖(L)🔍📄",
            "👨‍💻💾(S)💡",
            "🤖🔍🦋",
            "👤💬✅",
            "👨‍💻⚙️🌐➡️(L)💾✅"
        ]

        for s in sentences:
            translation = translator.translate(s)
            print(f"Věta: {s}\n  -> Překlad: {translation}\n")

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Došlo k neočekávané chybě: {e}")
