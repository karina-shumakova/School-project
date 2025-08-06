from buecher import Buecher

class Fantasy(Buecher):
    def __init__(self,p_genre,p_preis_pro_stuck,p_name,p_author,p_sprache):
        super().__init__(p_genre,p_preis_pro_stuck,p_name,p_author)
        self.sprache = str(p_sprache)
        
        
    def preisermitteln(self,gekauft):
        if self.sprache == "Englisch":
            preis = self.preis_pro_stuck * gekauft * 0.9
        else:
            preis = self.preis_pro_stuck * gekauft
        return round(preis,2)
               
        
    def begruessen(self):
        print("\nSie haben die Kategorie 'Fantasy' gewählt. \nNur heute: Für alle Bücher in englischer Sprache erhalten Sie 10% Rabatt.\n")
        
    
        