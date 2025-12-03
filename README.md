Emoji Prompt Language (EPL)

Tento repozitář obsahuje Proof of Concept (PoC) pro **Basic Emoji Language (EPL)**, jednoduchý jazyk založený na emoji pro efektivní komunikaci s AI.

Cílem tohoto projektu je demonstrovat, jak lze pomocí strukturovaných emoji vět:
- Výrazně snížit počet odesílaných tokenů.
- Zvýšit jednoznačnost a rychlost komunikace.
- Vytvořit intuitivní vizuální syntaxi pro složitější workflowy.

## Struktura Projektu

```
/BasicEmojiLanguage/
├── emojis.json             # Databáze všech Unicode emoji (slovník)
├── GRAMMAR.md              # Detailní specifikace gramatiky a pravidel jazyka EPL
├── GRAMMAR_MAP.json        # Vygenerovaný soubor s klíčovými gramatickými emoji
└── translator.py           # Hlavní skript (PoC) pro překlad EPL vět
```

## Jak to funguje

Skript `translator.py` je srdcem tohoto PoC.

1.  **Načte dva soubory:**
    - `emojis.json`: Velký slovník všech existujících emoji a jejich názvů.
    - `GRAMMAR_MAP.json`: Malý soubor definující klíčová "slova" gramatiky (jako `🚀` pro "start" nebo `🔍` pro "hledat").

2.  **Analyzuje větu:** Rozdělí emoji větu na jednotlivé symboly.

3.  **Překládá:**
    - Pro každý symbol zkontroluje, zda má definovanou **gramatickou roli** (Akce, Objekt, Subjekt...).
    - Pokud ano, použije jeho definovaný význam.
    - Pokud ne, najde jeho **obecný význam** v `emojis.json` (např. `🦋` -> "butterfly") a přiřadí mu výchozí roli "Objekt".

4.  **Sestaví výstup:** Z přeložených částí sestaví srozumitelnou anglickou větu.

## Jak spustit demo

1.  Otevřete terminál a ujistěte se, že jste v adresáři `Dokumenty`.
2.  Spusťte Python skript pomocí příkazu:

    ```bash
    python3 BasicEmojiLanguage/translator.py
    ```

3.  Skript nejprve vygeneruje `GRAMMAR_MAP.json` a poté vypíše překlady několika předdefinovaných EPL vět, aby demonstroval funkčnost.

## Další kroky

Tento PoC je jen začátek. Jazyk by se dal dále rozšířit například o:
- Podporu složitějších vnořených struktur.
- Přímé mapování na spustitelné funkce nebo API volání.
- Vytvoření plnohodnotného lexeru/parseru.
