import requests
import urllib.request
import time
from bs4 import BeautifulSoup


class Eisbach:
    def __init__(self):
        self.temperatur = "Unbekannt!"
        self.url = "https://www.gkd.bayern.de/de/fluesse/wassertemperatur/kelheim/muenchen-himmelreichbruecke-16515005/messwerte"
    
    def getTemperatur(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        one_a_tag = str(soup.findAll('td')[6])
        one_a_tag = one_a_tag.split(">")[1]
        one_a_tag = one_a_tag.split("<")[0]
        
        self.temperatur = one_a_tag

        return str(self.temperatur)