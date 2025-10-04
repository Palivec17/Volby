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
