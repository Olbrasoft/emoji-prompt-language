# -*- coding: utf-8 -*- 

import requests
from bs4 import BeautifulSoup
import json
import os
import re

def fetch_and_parse_emoji():
    """
    Stáhne a zpracuje HTML stránku s kompletním seznamem emoji z unicode.org.
    Pokud existuje lokální soubor 'unicode_page.html', použije ten.
    Rozdělí je do kategorií a uloží do samostatných JSON souborů.
    """
    local_html_file = "BasicEmojiLanguage/unicode_page.html"
    
    if os.path.exists(local_html_file):
        print(f"Nalezen lokální soubor {local_html_file}, zpracovávám jej.")
        with open(local_html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
    else:
        url = "https://unicode.org/emoji/charts/full-emoji-list.html"
        print(f"Stahuji data z {url}...")
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            html_content = response.content
        except requests.exceptions.RequestException as e:
            print(f"Chyba při stahování stránky: {e}")
            return

    print("Zpracovávám HTML...")
    soup = BeautifulSoup(html_content, 'html.parser')
    
    db_dir = "BasicEmojiLanguage/emoji_db"
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
        print(f"Vytvořen adresář: {db_dir}")

    all_categories = {}
    current_category = None
    table = soup.find('table')

    if not table:
        print("Chyba: V HTML nebyla nalezena žádná tabulka.")
        return

    for row in table.find_all('tr'):
        # Hledání nadpisu kategorie
        header = row.find('th', class_='bighead')
        if header and header.a:
            category_name = header.a.text.strip().lower()
            category_name = re.sub(r'[^\w\s-]', '', category_name) # Čištění názvu
            category_name = re.sub(r'[\s_]+', '-', category_name)
            current_category = category_name
            all_categories[current_category] = []
            print(f"Nalezena kategorie: {current_category}")
            continue

        if not current_category:
            continue

        # Hledání dat v řádku
        cells = row.find_all('td')
        if len(cells) > 5: # Potřebujeme dostatek buněk
            try:
                code_cell = row.find('td', class_='code')
                char_cell = row.find('td', class_='chars')
                name_cell = row.find('td', class_='name')

                if code_cell and char_cell and name_cell:
                    emoji_char = char_cell.text.strip()
                    emoji_name = name_cell.text.strip()
                    emoji_code = code_cell.text.strip()

                    if emoji_char and emoji_name:
                        all_categories[current_category].append({
                            "char": emoji_char,
                            "name": emoji_name,
                            "code": emoji_code
                        })
            except Exception:
                # Ignorovat řádky, které nemají očekávaný formát
                continue

    if not all_categories:
        print("Nepodařilo se extrahovat žádné kategorie emoji. Struktura HTML se mohla změnit.")
        return

    # Uložení kategorií a vytvoření indexu
    category_files = []
    for category, emojis in all_categories.items():
        if not emojis:
            print(f"Varování: Kategorie '{category}' je prázdná, nebude uložena.")
            continue
        file_path = os.path.join(db_dir, f"{category}.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(emojis, f, indent=2, ensure_ascii=False)
        category_files.append(f"{category}.json")
        print(f"Uloženo {len(emojis)} emoji do souboru {file_path}")

    index_path = os.path.join(db_dir, "index.json")
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump({"categories": sorted(category_files)}, f, indent=2, ensure_ascii=False)
    print(f"Vytvořen indexový soubor: {index_path}")
    
    print("\nZpracování dokončeno!")

if __name__ == "__main__":
    fetch_and_parse_emoji()