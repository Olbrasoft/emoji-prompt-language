je to blbost, nevěřte tomu. a hlavně šetří tokeny angličtina a ne emoji ikony. ale je to hezký, ty obrázky. 

<img width="978" height="1036" alt="image" src="https://github.com/user-attachments/assets/a23fa29d-f067-46cc-8dac-79d7ef793c3b" />


Emoji Prompt Language (EPL)

Tento repozitář obsahuje Proof of Concept (PoC) pro **Basic Emoji Language (EPL)**, jednoduchý jazyk založený na emoji pro efektivní komunikaci s AI.

Cílem tohoto projektu je demonstrovat, jak lze pomocí strukturovaných emoji vět:
- Výrazně snížit počet odesílaných tokenů.
- Zvýšit jednoznačnost a rychlost komunikace.
- Vytvořit intuitivní vizuální syntaxi pro složitější workflowy.

## Klíčový Případ Užití: Úspora Kontextového Okna pro AI Agenty

Moderní jazykové modely a AI agenti mají omezené **kontextové okno** (context window) – maximální množství textu, které dokáží zpracovat najednou. Velkou část tohoto okna často zabírají systémové instrukce a prompty, které agentovi říkají, jak se má chovat.

**Emoji Prompt Language (EPL) řeší tento problém.**

Tím, že v instrukčních `.md` souborech nahradíme běžná slova (především slovesa a koncepty jako "start", "hledat", "úspěch", "chyba") za jednopísmenové emoji, můžeme **drasticky zmenšit velikost těchto souborů**.

**Výhody:**
- **Více prostoru pro data:** Agentovi zbude více kapacity v kontextovém okně pro samotný úkol, historii konverzace a další dynamická data.
- **Rychlejší zpracování:** Méně textu na vstupu znamená rychlejší parsování a nižší latenci.
- **Nižší náklady:** U placených API se cena často odvíjí od počtu tokenů – EPL ji pomáhá snižovat.

V adresáři `/examples` najdete konkrétní ukázky porovnávající velikost instrukcí v běžném jazyce a v hybridním EPL formátu.

## Výsledky: Porovnání Velikosti

Následující tabulka ukazuje úsporu velikosti souboru při použití hybridního EPL formátu v porovnání s běžným textem v adresáři `/examples`.

| Příklad | Původní velikost (plain) | Velikost s EPL | Úspora |
| :--- | :--- | :--- | :--- |
| `agent_codegen` | 776 bajtů | 748 bajtů | **~3.6%** |
| `agent_system_prompt`| 770 bajtů | 750 bajtů | **~2.6%** |
| `global_instructions` | 18466 bajtů | 4631 bajtů | **~75%** |

*Poznámka: Ačkoliv se úspora u těchto krátkých příkladů může zdát malá, v reálných, komplexních systémových promptech s desítkami či stovkami instrukcí bude procentuální úspora mnohem výraznější a může uvolnit cenné místo v kontextovém okně.*

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
