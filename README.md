# EisbachTemperaturBot
## Warum?
- Sobald du dir denkst: "Ist der Eisbach gerade zu kalt zum schwimmen oder nicht?" kommt dieser Bot zu Verwendung

## Wie verwendest du diesen Bot?
1. Du verbindest dich erstmal mit ihm über diesen Link: https://t.me/eisbachtempbot
2. Du gibst /start ein um den Bot zu "starten"
3. Gib jedes mal /temp ein, wenn du die aktuellste Temperatur des Eisbachs bekommen willst

## Wie funktioniert dieser Bot=
1. Er bekommt den Befehl vom User die Temperatur zuschicken
2. Er lädt sich diese Seite runter: https://www.gkd.bayern.de/de/fluesse/wassertemperatur/kelheim/muenchen-himmelreichbruecke-16515005/messwerte/tabelle
3. Er holt sich die Tabelle raus und sucht nach dem ersten Wert der nicht "--" entspricht ("--" kommt vor, wenn kein Wert vorhanden ist)
4. Er schneidet daraufhin den übrigen HTML Text ab und schickt die Werte an den User