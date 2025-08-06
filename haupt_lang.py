from roman import Roman 
from fantasy import Fantasy
from krimi import Krimi
from kinderbuecher import Kinderbuch

print("Willkommen in unserem Buchladen! \nSchön, dass Sie da sind.\nBei einem Einkaufswert über 100 Euro erhalten Sie zusätzlich heute 10% Rabatt auf den Gesamtbetrag. \nHier sind einige Kategorien, die wir anbieten:")
print("\n1. Romane \n2. Fantasy \n3. Krimis und Thriller \n4. Kinderbücher \n5. !NEU! Gutschein")

totalsumme = 0
warenkorb = []

while True:
    try:
        wahl = input("Bitte wählen Sie eine Kategorie (1-5): ")
        
        
        if wahl == "1":
            romans = [
                Roman("Roman", 10.00, "Der alte Mann und das Meer", "Ernest Hemingway", "Deutsch"),
                Roman("Roman", 15.00, "1984", "George Orwell", "Englisch"),
                Roman("Roman", 3.50, "Moby Dick", "Herman Melville", "Deutsch"),
                Roman("Roman", 20.00, "Die Verwandlung", "Franz Kafka", "Deutsch"),
                Roman("Roman", 18.00, "Der Steppenwolf", "Hermann Hesse", "Deutsch")
                  ]
            romans[0].begruessen()
        
            for i, roman in enumerate(romans,1):
                print(i, end=". ")
                roman.aufzahlen()
                
            while True:
                try:
                    selected_book_number = int(input("Bitte geben Sie die Nummer des Buches ein, das Sie kaufen möchten: "))
                    if selected_book_number >= 1 and selected_book_number <= len(romans):
                        break
                    else:
                        print("Ungültige Auswahl. Bitte wählen Sie eine Zahl zwischen 1 und 5.")
                        continue
                except ValueError:
                    print("Geben Sie, bitte, eine Zahl ein!")
                        
            gekauft=int(input("Wieviele Exemplare möchten Sie kaufen? "))
            selected_roman = romans[selected_book_number - 1]
            preis = selected_roman.preisermittlen(gekauft)
            totalsumme = totalsumme + preis
            print("\nBuch wurde zum Warenkorb hinzugefügt. \nPreis:", preis, "€ \n ")
            warenkorb = warenkorb + [selected_roman.name + " - " + str(gekauft)+" St. " + str(preis)+"EUR"]
            
            
        
        elif wahl == "2":
            
            fantasybook = [
                Fantasy("Fantasy", 13.00, "Der Herr der Ringe", "J.R.R. Tolkien", "Deutsch"),
                Fantasy("Fantasy", 15.50, "Harry Potter", "J.K. Rowling", "Englisch"),
                Fantasy("Fantasy", 10.30, "Die Chroniken von Narnia", "C.S. Lewis", "Englisch"),
                Fantasy("Fantasy", 7.00, "Das Lied von Eis und Feuer", "George R.R. Martin", "Deutsch"),
                Fantasy("Fantasy", 9.00, "Der Name des Windes", "Patrick Rothfuss", "Deutsch"),
                ]
            
            fantasybook[0].begruessen()
        
            i = 1
            for fantasy in fantasybook:
                print(i, end=". ")
                fantasy.aufzahlen()
                i= i+1
                
            while True:
                try:
                    selected_book_number = int(input("Bitte geben Sie die Nummer des Buches ein, das Sie kaufen möchten: "))
                    if selected_book_number >= 1 and selected_book_number <= len(fantasybook):
                        break
                    else:
                        print("Ungültige Auswahl. Bitte wählen Sie eine Zahl zwischen 1 und 5.")
                        continue
                except ValueError:
                    print("Geben Sie, bitte, eine Zahl ein!")
                    
            selected_fantasy = fantasybook[selected_book_number - 1]
            gekauft=int(input("Wieviele Exemplare möchten Sie kaufen? "))
            preis = selected_fantasy.preisermittlen(gekauft)
            totalsumme = totalsumme + preis
            print("\nBuch wurde zum Warenkorb hinzugefügt. \nPreis:", preis, "€ \n ")
            warenkorb = warenkorb + [selected_fantasy.name + " - " + str(gekauft)+" St. " + str(preis)+"EUR"]
            
            
            
        elif wahl == "3":
            krimis = [
                Krimi("Krimi", 11.50, "Der Richter und sein Henker", "Friedrich Dürrenmatt", "Deutsch",1950),
                Krimi("Krimi", 12.50, "Mord im Orientexpress", "Agatha Christie", "Deutsch",1934),
                Krimi("Krimi", 9.99, "Das Schweigen der Lämmer", "Thomas Harris", "Englisch",1988),
                Krimi("Krimi", 8.75, "Verblendung", "Stieg Larsson", "Deutsch",2005),
                Krimi("Krimi", 10.00, "Der Name der Rose", "Umberto Eco", "Deutsch",1980),
                ]

            
            krimis[0].begruessen()
        
            i = 1
            for krimi in krimis:
                print(i, end=". ")
                krimi.aufzahlen()
                i= i+1
                
            while True:
                try:
                    selected_book_number = int(input("Bitte geben Sie die Nummer des Buches ein, das Sie kaufen möchten: "))
                    if selected_book_number >= 1 and selected_book_number <= len(krimis):
                        break
                    else:
                        print("Ungültige Auswahl. Bitte wählen Sie eine Zahl zwischen 1 und 5.")
                        continue
                except ValueError:
                    print("Geben Sie, bitte, eine Zahl ein!")
                    
            selected_krimi = krimis[selected_book_number - 1]
            gekauft=int(input("Wieviele Exemplare möchten Sie kaufen? "))
            preis = selected_krimi.preisermittlen(gekauft)
            totalsumme = totalsumme + preis
            print("\nBuch wurde zum Warenkorb hinzugefügt.\nPreis:", preis, "€ \n ")
            warenkorb = warenkorb + [selected_krimi.name +" - " + str(gekauft)+" St. " + str(preis)+"EUR"]
            
            
        
        elif wahl == "4":
            kinderbuecher = [
                Kinderbuch("Kinderbuch", 10.75, "Der kleine Prinz", "Antoine de Saint-Exupéry", "Englisch"),
                Kinderbuch("Kinderbuch", 6.50, "Oh, wie schön ist Panama", "Janosch", "Deutsch"),
                Kinderbuch("Kinderbuch", 8.00, "The Gruffalo", "Julia Donaldson", "Deutsch"),
                ]

            
            kinderbuecher[0].begruessen()
        
            i = 1
            for kinderb in kinderbuecher:
                print(i, end=". ")
                kinderb.aufzahlen()
                
                i= i+1
                
            while True:
                try:
                    selected_book_number = int(input("Bitte geben Sie die Nummer des Buches ein, das Sie kaufen möchten: "))
                    if selected_book_number >= 1 and selected_book_number <= len(kinderbuch):
                        break
                    else:
                        print("Ungültige Auswahl. Bitte wählen Sie eine Zahl zwischen 1 und 5.")
                        continue
                except ValueError:
                    print("Geben Sie, bitte, eine Zahl ein!")
                    
            selected_kinderbuch = kinderbuecher[selected_book_number - 1]
            gekauft=int(input("Wieviele Exemplare möchten Sie kaufen? "))
            zahlende_exemplare = gekauft - (gekauft // 3)
            preis = selected_kinderbuch.preisermittlen(zahlende_exemplare,gekauft)
            totalsumme = totalsumme + preis
            print("\nBuch wurde zum Warenkorb hinzugefügt.\nPreis:", preis, "€ \n ")
            warenkorb = warenkorb + [selected_kinderbuch.name +" - " + str(gekauft)+" St. " + str(preis)+"EUR"]
            
            
            
        elif wahl == "5":
            print("\nSie haben die Option gewählt, einen Gutschein zu kaufen.")
            
            while True:
                try:
                    gutschein_betrag = float(input("Bitte geben Sie den gewünschten Gutscheinbetrag in Euro ein: "))
                    if gutschein_betrag <= 0:
                        print("Der Betrag muss größer als 0 sein. Bitte versuchen Sie es erneut.")
                        continue
                    break
                except ValueError:
                    print("Ungültige Eingabe! Bitte geben Sie eine gültige Zahl ein.")
                    
            totalsumme = totalsumme + gutschein_betrag
            warenkorb = warenkorb + ["Gutschein - "+str(gutschein_betrag)]
            
            
            
        else:
            print("Ungültige Auswahl. Bitte wählen Sie eine Zahl zwischen 1 und 5.")
            continue
            
        
        
        
        sehen = input("Wollen Sie den Warenkorb sehen? (ja/nein): ").lower()
        while sehen != "ja" and sehen != "nein":
            print("!Ungültige Eingabe. Bitte geben Sie 'ja' oder 'nein' ein!")
            sehen = input("Wollen Sie den Warenkorb sehen? (ja/nein): ").lower()
        if sehen == "ja":
            for buch in warenkorb:
                print("-", buch)
            if totalsumme > 100:
                rabatt = 0.1 * totalsumme
                endbetrag = totalsumme - rabatt
                print("Sie erhalten 10% Rabatt, neue Endbetrag: ", round(endbetrag, 2), "EUR")
            else:
                print("Endbetrag:", round(totalsumme,2), "EUR")
                
                
                
            
        weiter = input("Möchten Sie weiter einkaufen? (ja/nein): ").lower()
        
        while weiter != "ja" and weiter != "nein":
            print("!Ungültige Eingabe. Bitte geben Sie 'ja' oder 'nein' ein!")
            weiter = input("Möchten Sie weiter einkaufen? (ja/nein): ").lower()
        
        if weiter == "nein":
            print("\nVielen Dank für Ihren Einkauf!")
            print("Hier ist Ihr Warenkorb:")
            
            for buch in warenkorb:
                print("-", buch)
            if totalsumme >100:
                rabatt = 0.1 * totalsumme
                endbetrag = totalsumme - rabatt
                print("Sie erhalten 10% Rabatt, neue Endbetrag: ", round(endbetrag,2), "EUR")
            else:
                print("Endbetrag:", totalsumme, "EUR")
            print("Wir wünschen Ihnen einen schönen Tag!")

            break
        
        
    except ValueError:
        print("Geben Sie, bitte, eine Zahl ein!")