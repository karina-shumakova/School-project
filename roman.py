from buecher import Buecher

class Roman(Buecher):
    def __init__(self,p_genre,p_preis_pro_stuck,p_name,p_author,p_sprache):
        super().__init__(p_genre,p_preis_pro_stuck,p_name,p_author)
        self.sprache = str(p_sprache)
        
        
    
    def preisermitteln(self,gekauft):
        if gekauft >= 5:
            preis = self.preis_pro_stuck * gekauft * 0.8  # 20% rabatt
        else:
            preis = self.preis_pro_stuck * gekauft
        return round(preis,2) 
       
        
    def begruessen(self):
        print("\nSie haben die Kategorie 'Romane' gewählt. \nNur heute: Beim Kauf von mindestens 5 Exemplaren eines Romans erhalten Sie 20% Rabatt. \n")
        
    