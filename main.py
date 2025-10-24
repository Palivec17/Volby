"""
main.py: třetí projekt do Engeto Online Python Akademie

author: Petr Polívka
email: palivec17@seznam.cz
"""


import sys
import requests
from bs4 import BeautifulSoup
import csv



# Zadané argumenty
def validate_arguments(args):
    if len(args) != 3:
        print("❌ Chyba: Zadejte 2 argumenty – URL a název výstupního souboru.")
        sys.exit(1)
    if not args[1].startswith("https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ"):
        print("❌ Chyba: První argument musí být platný odkaz na územní celek.")
        sys.exit(1)

# Odkazy na obce
def get_obec_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = []
    for a in soup.find_all("a"):
        href = a.get("href")
        if href and "xobec=" in href:
            full_url = "https://www.volby.cz/pls/ps2017nss/" + href
            links.append(full_url)
    return links



# Data z obcí
def scrape_obec_data(obec_url):
    response = requests.get(obec_url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Získání názvu a kódu obce
    obec_info = soup.find("h3").text.strip()
    kod_obce = obec_info.split(":")[0].strip()
    nazev_obce = obec_info.split(":")[1].strip()

    # Získání údajů o voličích
    tds = soup.find_all("td")
    volici = tds[3].text.strip()
    obalky = tds[4].text.strip()
    platne_hlasy = tds[7].text.strip()

    # Získání hlasů pro strany
    strany = {}
    tables = soup.find_all("table")[1:]
    for table in tables:
        rows = table.find_all("tr")[2:]
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 2:
                nazev_strany = cols[1].text.strip()
                hlasy = cols[2].text.strip()
                strany[nazev_strany] = hlasy

    return {
        "Kód obce": kod_obce,
        "Název obce": nazev_obce,
        "Voliči v seznamu": volici,
        "Vydané obálky": obalky,
        "Platné hlasy": platne_hlasy,
        **strany
    }




# Hlavní funkce
def main():
    validate_arguments(sys.argv)
    url = sys.argv[1]
    output_file = sys.argv[2]

    obec_links = get_obec_links(url)
    vysledky = []
    vsechny_strany = set()

    print(f"Nalezeno obcí: {len(obec_links)}")

    for obec_url in obec_links:
        print(f"Zpracovávám: {obec_url}")
        try:
            data = scrape_obec_data(obec_url)
            vysledky.append(data)
            vsechny_strany.update(data.keys() - {"Kód obce", "Název obce", "Voliči v seznamu", "Vydané obálky", "Platné hlasy"})
            print(f"→ {data['Název obce']} ({data['Kód obce']})")
        except Exception as e:
            print(f"⚠️ Chyba při zpracování obce: {obec_url}")
            print(f"   → {e}")

        
# Uložení do CSV
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Kód obce", "Název obce", "Voliči v seznamu", "Vydané obálky", "Platné hlasy"] + sorted(vsechny_strany)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in vysledky:
            writer.writerow(row)





# Spuštění
if __name__ == "__main__":
    main()


