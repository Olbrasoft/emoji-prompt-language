Emoji Prompt Language (EPL) - Specifikace Gramatiky

## 1. Úvod a Filozofie

**Basic Emoji Language (EPL)** je ultra-lehký, doménově-specifický jazyk (DSL) navržený pro efektivní a jednoznačnou komunikaci mezi člověkem a AI.

**Hlavní cíle:**
- **Úspora tokenů:** Drasticky snižuje počet tokenů potřebných pro komunikaci (až o 80-90 % oproti přirozenému jazyku).
- **Jednoznačnost:** Minimalizuje riziko halucinací a nepochopení díky pevně dané gramatice.
- **Rychlost:** Méně tokenů znamená rychlejší zpracování a odezvu od AI.
- **Intuitivnost:** Využívá vizuální a sekvenční logiku, která je pro lidi přirozená.

## 2. Základní Principy

1.  **Pořadí Emoji = Syntax:** Vztahy mezi emoji jsou dány jejich pořadím, ne textem.
2.  **Struktura Subjekt-Akce-Objekt:** Jazyk se inspiruje přirozenými jazyky a vizuální gramatikou (jak ji popsal např. Neil Cohn).
3.  **Bracketing:** Akce nebo workflow mohou být "zabaleny" do otevíracích a zavíracích symbolů.
4.  **Krátké Sekvence:** Věty jsou krátké (ideálně 3-10 emoji), aby zůstaly čitelné a efektivní.
5.  **Rozšiřitelnost:** Slovník je dán `emojis.json`, ale významy pro gramatiku jsou definovány v parseru a lze je snadno rozšířit.

## 3. Struktura Věty

Věta v EPL se skládá z definovaných částí. Ne všechny jsou povinné.

**`[SUBJEKT] [AKCE] [OBJEKT] [MODIFIKÁTOR] [STAV/KONEC]`**

| Část | Popis | Příklady | Význam |
| :--- | :--- | :--- | :--- |
| **Subjekt** | Kdo/co provádí akci. Pokud chybí, výchozí je `👤` (člověk). | `👤`, `🤖`, `👨‍💻`, `🏢` | Člověk, AI, programátor, systém... |
| **Akce** | Hlavní sloveso věty. Co se děje. Povinná část. | `🚀` (start), `🔍` (hledat), `⚙️` (nastavit), `💾` (uložit) | Start, Hledání, Konfigurace, Uložení... |
| **Objekt** | Na co/koho se akce vztahuje. | `📄` (soubor), `🗪` (diskuze), `💡` (nápad), `🌐` (web) | Soubor, Diskuze, Nápad, Web... |
| **Modifikátor**| Upřesňuje akci nebo objekt. | `✅` (pozitivní), `❌` (negativní), `➡️` (další), `🔄` (opakovat), `💬💬` (opakování) | Potvrzení, Chyba, Pokračování, Smyčka, Trvání... |
| **Stav/Konec**| Uzavírá větu nebo sekvenci, potvrzuje stav. | `✅` (hotovo), `❌` (selhalo), `🔔` (notifikace), `❓` (otázka) | Hotovo, Chyba, Notifikace, Otázka... |

## 4. Modifikátory Důrazu (Velikost)

Pro přidání další sémantické vrstvy zavádíme modifikátory důrazu, které vizuálně reprezentují "velikost" nebo "důležitost" akce či objektu.

- **Syntaxe:** Značka se píše těsně před emoji, které modifikuje.
- `(L)` - **Large/Vysoký důraz**: Znamená, že akce je urgentní, důležitá, nebo že objekt je hlavní.
- `(S)` - **Small/Nízký důraz**: Znamená, že akce je podružná, nebo že objekt je méně důležitý.

**Příklady:**
- **`(L)🚀`**: "Důrazně spouští" / "Urgentní start".
- **`(S)📄`**: "Méně důležitý soubor" / "Poznámka na okraj".

## 5. Příklady Použití

### Příklad 1: Urgentní akce

**Věta:** `🤖(L)💾📄`
- **Překlad:** AI urgentně ukládá soubor.
- **Struktura:** `[SUBJEKT] [MODIFIKÁTOR_DŮRAZU] [AKCE] [OBJEKT]`

### Příklad 2: Komplexní workflow s důrazem

**Věta:** `👨‍💻🗪🚀 (L)⚙️🌐 ➡️ (S)💾✅ 🗪✅`
- **Překlad:** Programátor zahájil workflow: primárně nakonfiguroval web, poté jako vedlejší krok úspěšně uložil a workflow uzavřel.
- **Úspora tokenů:** I s modifikátory je úspora stále obrovská.

### Příklad 3: Podmínka a chyba

**Věta:** `🤖🔄📄❓ ➡️ ✅ | (L)❌🔔`
- **Překlad:** AI se v cyklu dotazuje na stav souboru. Pokud je v pořádku, pokračuj. Jinak (pokud chyba), pošli urgentní notifikaci.

## 6. Slovník (`emoji_db/`)

Jazyk používá standardní Unicode emoji. Jejich konkrétní gramatický význam (zda jsou Akce, Objekt atd.) je definován v logice parseru. Tento přístup umožňuje flexibilitu – např. `💾` může být v jednom kontextu akce "uložit", v jiném objekt "disketa".

---
*Tento dokument je živý a může se vyvíjet s dalšími nápady a potřebami.*
