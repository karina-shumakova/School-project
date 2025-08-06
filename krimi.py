from buecher import Buecher

class Krimi(Buecher):
    def __init__(self,p_genre,p_preis_pro_stuck,p_name,p_author,p_sprache):
        super().__init__(p_genre,p_preis_pro_stuck,p_name,p_author)
        self.sprache = str(p_sprache)
        
        
        
    
    def preisermitteln(self,gekauft):
        preis = self.preis_pro_stuck * gekauft
        return round(preis,2) 
       
        
    def begruessen(self):
        print("\nSie haben die Kategorie 'Krimi' gewählt. \n")
        
