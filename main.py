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
        print("❌ Chyba: Musíte zadat přesně dva argumenty – URL a název výstupního souboru.")
        print("Použití: python main.py <platná_URL> <výstupní_soubor.csv>")
        sys.exit(1)
    if not args[1].startswith("https://www.volby.cz/pls/ps2017nss/"):
        print("❌ Chyba: První argument musí být platná URL začínající na 'https://www.volby.cz/pls/ps2017nss/'.")
        sys.exit(1)

# Odkazy na obce
def get_obec_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = []
    for a in soup.find_all("a"):
        href = a.get("href")
        if href and "xobec" in href:
            full_url = "https://www.volby.cz/pls/ps2017nss/" + href
            links.append(full_url)
    return links


# Data z obcí
def scrape_obec_data(obec_url):
    response = requests.get(obec_url)
    soup = BeautifulSoup(response.content, "html.parser")

    kod_obce = soup.find("h3").text.split(":")[0].strip()
    nazev_obce = soup.find("h3").text.split(":")[1].strip()

    tables = soup.find_all("table")
    volici_data = tables[0].find_all("td")
    volici = volici_data[3].text.strip()
    obalky = volici_data[4].text.strip()
    platne_hlasy = volici_data[7].text.strip()

    strany = {}
    for table in tables[1:]:
        rows = table.find_all("tr")[2:]
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 2:
                nazev_strany = cols[1].text.strip()
                hlasy = cols[2].text.strip()
                strany[nazev_strany] = hlasy


