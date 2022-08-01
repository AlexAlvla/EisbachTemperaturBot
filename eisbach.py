import requests
from bs4 import BeautifulSoup


class Eisbach:
    def __init__(self):
        self.temperatur = "Unbekannt!"
        self.date = "Unbekannt!"
        self.url = "https://www.gkd.bayern.de/de/fluesse/wassertemperatur/kelheim/muenchen-himmelreichbruecke-16515005/messwerte/tabelle"
        self.row = 4
        self.one_a_tag = "--"
        self.result = "Leider keine Daten :/"
    
    def getTemperatur(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")


        # Getting data so long as needed
        while self.one_a_tag == "--":
            self.row = self.row + 2
            self.one_a_tag = str(soup.findAll('td')[self.row])
            self.one_a_tag = self.one_a_tag.split(">")[1]
            self.one_a_tag = self.one_a_tag.split("<")[0]

        # set the temperatur to the temperatur of the scrapper    
        self.temperatur = self.one_a_tag

        # getting date of the data
        self.date = str(soup.findAll('td')[self.row - 1])
        self.date = self.date.split(">")[1]
        self.date = self.date.split("<")[0]

        self.result = "Der aktuellste Wert ist: " + str(self.temperatur) + "C\nDieser Wert ist vom: " + str(self.date)

        return str(self.result)