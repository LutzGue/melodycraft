import json
import random

def generate_melody(song_data):
    melody = []

    for taktbereich in song_data["taktbereich"]:
        start = taktbereich["start"]
        ende = taktbereich["ende"]
        verlauf = taktbereich["verlauf"]
        tonmaterial = taktbereich["tonmaterial"]
        notenserie = taktbereich["notenserie"]

        if verlauf["arc"]["typ"] == "hoch":
            # Implementiere Logik für den Verlaufstyp "arc"
            pass
        elif verlauf["linie"]["typ"] == "statisch":
            # Implementiere Logik für den Verlaufstyp "linie"
            pass

        # Implementiere Logik für die Tonmaterialien (romanchord und diatonisch)
        # Beachte die Mindest- und Höchstwerte der Notenserie

    return melody

def main():

    # Lese die JSON-Datei ein
    with open("example1.json", "r") as file:
        song_data = json.load(file)

    # Generiere die Melodie basierend auf den Daten in der JSON-Datei
    #melody = generate_melody(song_data)

    # Zeige die generierte Melodie an (oder speichere sie, wie gewünscht)
    #print("Generierte Melodie:", melody)

if __name__ == "__main__":
    main()
