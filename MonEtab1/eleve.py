class Eleve:
    def __init__ (self, id, nom, prenom, age, genre):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.genre = genre
    
    def __str__ (self):
        return f"{self.id},{self.nom},{self.prenom},{self.age},{self.genre}"   
    
        
