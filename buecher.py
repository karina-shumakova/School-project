from abc import ABC, abstractmethod

class Buecher(ABC):
    def __init__(self,p_genre,p_preis_pro_stuck,p_name,p_author):
        self.genre = str(p_genre)
        self.preis_pro_stuck = float(p_preis_pro_stuck)
        self.name = str(p_name)
        self.author = str(p_author)
        
    
    @abstractmethod    
    def begruessen(self):
        pass
        
    def preisermitteln(self):
        pass
            
    def aufzahlen(self):  
        print(self.name + "," , self.author+", ("+ self.sprache +") -",self.preis_pro_stuck,"EUR \n ")
    
    