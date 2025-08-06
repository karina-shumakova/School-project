from roman import Roman 
from fantasy import Fantasy
from krimi import Krimi
from kinderbuecher import Kinderbuch

def buchauswahl(max_anzahl):
    while True:
        try:
            buchauswahl = int(input("Bitte geben Sie die Nummer des Buches ein, das Sie kaufen möchten: "))
            if buchauswahl >= 1 and buchauswahl <= max_anzahl:
                return buchauswahl

            else:
                print("Ungültige Auswahl. Bitte wählen Sie eine Zahl zwischen 1 und 5.")
                continue
        except ValueError:
            print("Geben Sie, bitte, eine Zahl ein!")
    
def anzahlauswahl():
    while True:
        try:
            auswahl=int(input("Wieviele Exemplare möchten Sie kaufen? "))
            assert auswahl >=1
            return auswahl
        except ValueError:
            print("Geben Sie, bitte, eine Zahl ein!")
        except AssertionError:
            print("Geben Sie eine positive Zahl ein!")
            
            
def buchkaufen(buecherliste,totalsumme,warenkorb):
    buecherliste[0].begruessen()
    for i, buch in enumerate(buecherliste, 1):
        print(i, end=". ")
        buch.aufzahlen()
        
    ausgewählte_buch = buchauswahl(len(buecherliste))                
    gekauft = anzahlauswahl()  
    buch = buecherliste[ausgewählte_buch - 1]
    preis = buch.preisermitteln(gekauft)
    totalsumme += preis
    print("\nBuch wurde zum Warenkorb hinzugefügt. \nPreis:", preis, "€","\nTotalpreis: ", totalsumme, "€")
    warenkorb.append(buch.name + " , " + str(gekauft) + " St. = " + str(round(preis, 2)) + " EUR")
    return totalsumme,warenkorb

def warenkorbzeigen(totalsumme,warenkorb):
    print("\nIhr Warenkorb:")
    for buch in warenkorb:
        print("- ", buch)
    if totalsumme >100:
        rabatt = 0.1 * totalsumme
        endbetrag = totalsumme - rabatt
        print("Totalsumme: ",totalsumme)
        print("Sie erhalten 10% Rabatt, neue Endbetrag: ", round(endbetrag,2), "EUR")
    else:
        print("Endbetrag:", totalsumme, "EUR")




print("Willkommen in unseren Buchladen! \nSchön, dass Sie da sind.\nBei einem Einkaufswert über 100 Euro erhalten Sie zusätzlich heute 10% Rabatt auf den Gesamtbetrag.")
print("Hier sind einige Kategorien, die wir anbieten:")
print("\n1. Romane \n2. Fantasy \n3. Krimis und Thriller \n4. Kinderbücher \n5. !NEU! Gutschein")

totalsumme = 0
warenkorb = []

while True:
    try:
        wahl = int((input("Bitte wählen Sie eine Kategorie (1-5): ")))
        
         
        if wahl == 1:
            romans = [
                Roman("Roman", 10.00, "Der alte Mann und das Meer", "Ernest Hemingway", "Deutsch"),
                Roman("Roman", 15.70, "1984", "George Orwell", "Englisch"),
                Roman("Roman", 3.50, "Moby Dick", "Herman Melville", "Deutsch"),
                Roman("Roman", 20.00, "Die Verwandlung", "Franz Kafka", "Deutsch"),
                Roman("Roman", 18.00, "Der Steppenwolf", "Hermann Hesse", "Deutsch")
                  ]
            totalsumme, warenkorb = buchkaufen(romans,totalsumme,warenkorb)            
        
        elif wahl == 2:
            
            fantasybook = [
                Fantasy("Fantasy", 13.00, "Der Herr der Ringe", "J.R.R. Tolkien", "Deutsch"),
                Fantasy("Fantasy", 15.50, "Harry Potter", "J.K. Rowling", "Englisch"),
                Fantasy("Fantasy", 10.30, "Die Chroniken von Narnia", "C.S. Lewis", "Englisch"),
                Fantasy("Fantasy", 7.00, "Das Lied von Eis und Feuer", "George R.R. Martin", "Deutsch"),
                Fantasy("Fantasy", 9.00, "Der Name des Windes", "Patrick Rothfuss", "Deutsch"),
                ]
                
            totalsumme, warenkorb = buchkaufen(fantasybook,totalsumme,warenkorb)
            
            
            
        elif wahl == 3:
            krimis = [
                Krimi("Krimi", 11.50, "Der Richter und sein Henker", "Friedrich Dürrenmatt", "Deutsch"),
                Krimi("Krimi", 12.50, "Mord im Orientexpress", "Agatha Christie", "Deutsch"),
                Krimi("Krimi", 9.99, "Das Schweigen der Lämmer", "Thomas Harris", "Englisch"),
                Krimi("Krimi", 8.75, "Verblendung", "Stieg Larsson", "Deutsch"),
                Krimi("Krimi", 10.00, "Der Name der Rose", "Umberto Eco", "Deutsch"),
                ]

            
            totalsumme, warenkorb = buchkaufen(krimis,totalsumme,warenkorb)
            
            
        
        elif wahl == 4:
            kinderbuecher = [
                Kinderbuch("Kinderbuch", 10.75, "Der kleine Prinz", "Antoine de Saint-Exupéry", "Englisch"),
                Kinderbuch("Kinderbuch", 6.50, "Oh, wie schön ist Panama", "Janosch", "Deutsch"),
                Kinderbuch("Kinderbuch", 8.00, "The Gruffalo", "Julia Donaldson", "Deutsch"),
                ]

            
            totalsumme, warenkorb = buchkaufen(kinderbuecher,totalsumme,warenkorb)
            
            
            
        elif wahl == 5:
            print("\nSie haben die Option gewählt, einen Gutschein zu kaufen.")
            
            while True:
                try:
                    gutschein_betrag = float(input("Bitte geben Sie den gewünschten Gutscheinbetrag in Euro ein: "))
                    if gutschein_betrag < 10:
                        print("Der Betrag muss größer als 10 sein. Bitte versuchen Sie es erneut.")
                        continue
                    print("Gutschein wurde zum Warenkorb hinzugefügt.")
                    break
                except ValueError:
                    print("Ungültige Eingabe! Bitte geben Sie eine gültige Zahl größer als 10 ein.")
                    
            totalsumme = totalsumme + gutschein_betrag
            warenkorb.append("Gutschein - "+str(gutschein_betrag))
            
            
            
        else:
            print("Ungültige Auswahl. Bitte wählen Sie eine Zahl zwischen 1 und 5.")
            continue
            
        
        
        
        sehen = input("\nWollen Sie den Warenkorb sehen? (ja/nein): ").lower().strip()
        while sehen != "ja" and sehen != "nein":
            print("!Ungültige Eingabe. Bitte geben Sie 'ja' oder 'nein' ein!")
            sehen = input("Wollen Sie den Warenkorb sehen? (ja/nein): ").lower().strip()
        if sehen == "ja":
            warenkorbzeigen(totalsumme,warenkorb)
                
                
                
            
        weiter = input("\nMöchten Sie weiter einkaufen? (ja/nein): ").lower().strip()
        
        while weiter != "ja" and weiter != "nein":
            print("!Ungültige Eingabe. Bitte geben Sie 'ja' oder 'nein' ein!")
            weiter = input("Möchten Sie weiter einkaufen? (ja/nein): ").lower().strip()
        
        if weiter == "nein":
            print("\nVielen Dank für Ihren Einkauf!")
            warenkorbzeigen(totalsumme,warenkorb)
            print("Wir wünschen Ihnen einen schönen Tag!")
            break
        
        
    except ValueError:
        print("Geben Sie, bitte, eine Zahl ein!")
        
        