import requests
from bs4 import BeautifulSoup


class Eisbach:
    def __init__(self):
        self.temperatur = "Unbekannt!"
        self.url = "https://www.gkd.bayern.de/de/fluesse/wassertemperatur/kelheim/muenchen-himmelreichbruecke-16515005/messwerte"
        self.row = 6
        self.one_a_tag = "--"
    
    def getTemperatur(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")

        while self.one_a_tag == "--" and self.row <= 18:
            self.one_a_tag = str(soup.findAll('td')[self.row])
            self.one_a_tag = self.one_a_tag.split(">")[1]
            self.one_a_tag = self.one_a_tag.split("<")[0]
            self.row = self.row + 2
                
        if(self.one_a_tag != "--"):
            self.temperatur = self.one_a_tag


        return str(self.temperatur)