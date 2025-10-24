Tento projekt vytvořil Petr Polívka jako třetí úkol v rámci Engeto Online Python Akademie.

# Analýza volebních výsledků

Tento projekt slouží ke scrapování volebních dat z webu [volby.cz](https://www.volby.cz/) pro volby do Poslanecké sněmovny ČR v roce 2017. Výsledky jsou ukládány do CSV souboru pro další analýzu.

## 📦 Instalace

1. Vytvořte si virtuální prostředí:
    # python -m venv volby_env

2. Aktivujte prostředí:
    # Windows:
  ```
  .\\volby_env\\Scripts\\activate
  ```
    # macOS/Linux:
  ```
  source volby_env/bin/activate
  ```


3. Projekt využívá následující knihovny:

    # `requests`
    #`beautifulsoup4`

Instalace pomocí `requirements.txt`:


```bash
pip install -r requirements.txt


4. 🚀 Spuštění projektu
    # Skript se spouští pomocí dvou argumentů:

URL na konkrétní územní celek (např. okres, obec)
Název výstupního CSV souboru

    # Příklad - 
        python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xobec=548481" "vysledky_havlickuv_brod.csv"

        Tento příkaz stáhne volební výsledky pro obec Havlíčkův Brod a uloží je do souboru vysledky_havlickuv_brod.csv.

⚠️ Chybové hlášky

Pokud nejsou zadány oba argumenty, skript skončí s upozorněním.
Pokud je URL neplatná nebo nevede na stránku s daty, skript vypíše chybu a pokračuje dál.

5. 📁 Výstup
    # Výstupem je CSV soubor s následujícími sloupci:

Kód obce
Název obce
Voliči v seznamu
Vydané obálky
Platné hlasy
Hlasy pro jednotlivé strany
