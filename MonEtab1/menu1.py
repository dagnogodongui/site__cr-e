import time
eleves = {}
note = {}
matiere = {}
#afficher le menu
def afficher_menu():
    print( " ----Akwaba dans l'application MonEtab----")
    print("1: ajouter un éleve")
    print("2: supprimer un eleve")
    print("3: modifier les information de l'eleve")
    print("4: lister les eleves")
    print("5: gerer les notes")
    print("6: quitter")
# creer la classe Eleve
class Eleve:
    def __init__(self, id, nom, prenom, age, genre, note ):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.note= note
        self.genre = genre
    def __str__(self):
        return f"Eleve(id={self.id}, nom ={self.nom}, prenom={self.prenom}, age = {self.age}, genre ={self.genre}, note={self.note})"
# creer la classe MATIERE    
class Matiere:
    def __init__(self, id, nom):
        self.id = id
        self.nom = nom
    def __str__(self):
        return f"Eleve(id={self.id}, nom ={self.nom})"

class note:
    def __init__(self, id, valeur, Eleve, note):
        self.id = id
        self.valeur = valeur
        self.Eleve = Eleve
        self.note = note
    def __str__(self):
        return f"Eleve(id={self.id}, valeur ={self.valeur}, eleve={self.Eleve}, note = {self.note})"
# Ajouter un eleve
def ajouter_eleve():
    id_eleve = input("Entrez id de l'élève: ")
    if id_eleve in eleves:
        print("Cet id existe déjà.")
        return
    
    nom = input("Entrez le nom de l'élève: ")
    prenom = input("Entrez le prénom de l'élève: ")
    age = input("Entrez l'âge de l'élève: ")
    genre = input("Entrez le genre de l'élève: ")

    eleves[id_eleve] = {'Nom': nom, 'Prénom': prenom, 'Âge': age, 'Genre': genre}
    print(f"\nÉlève ajouté : {eleves[id_eleve]}")
#modifier un eleve
def modifier_eleve():
    id_eleve = input("Entrez id de l'élève à modifier: ")
    if id_eleve not in eleves:
        print("Cet élève n'existe pas.")
        return
    #print("\nSous-options de modification:")
    while True:
        print("1. Modifier le nom")
        print("2. Modifier le prénom")
        print("3. Modifier la date de naissance (Ex:// )")
        print("4. Modifier l'identifiant")
        print("5. Retour")
        print("6. Accueil")

        choix = input("Choisissez une option: ")
        
        if choix == '1':
            nouveau_nom = input("Entrez le nouveau nom: ")
            eleves[id_eleve]['Nom'] = nouveau_nom
        elif choix == '2':
            nouveau_prenom = input("Entrez le nouveau prénom: ")
            eleves[id_eleve]['Prénom'] = nouveau_prenom
        elif choix == '3':
            nouvelle_date_naissance = input("Entrez la nouvelle date de naissance (Ex: 23/12/1998): ")
            eleves[id_eleve]['Date de naissance'] = nouvelle_date_naissance
        elif choix == '4':
            nouveau_id_eleve = input("Entrrez id: ")
            if nouveau_id_eleve in eleves:
                print("Cet identifiant existe déjà.")
            else:
                eleves[nouveau_id_eleve] = eleves.pop(id_eleve)
        elif choix == '5':
            return
        elif choix == '6':
            break
        print(f"\nInformations modifiées : {eleves[id_eleve]}")
        # Gestion de l'accueil ou du menu principal

        print(f"\nInformations modifiées : {eleves[id_eleve]}")

def lister_eleves():
    if not Eleve:
        print("Aucun élève enregistré.")
        return
    
    print("\nListe des élèves:")
    for id_eleve, infos in eleves.items():
        print(f"ID: {id_eleve}, Infos: {infos}")

#ajouter une note
def ajouter_note():
    id_eleve = input("Entrez l'identifiant unique de l'élève: ")
    if id_eleve not in eleves:
        print("Cet élève n'existe pas.")
        return
    
    matiere = input("Entrez la matière: ")
    note = input("Entrez la note: ")
    
    if id_eleve not in note:
        note[id_eleve] = {}
    
    note[id_eleve][matiere] = note
    print("Note ajoutée.")
#modifier une note
def modifier_note():
    id_eleve = input("Entrez l'identifiant unique de l'élève: ")
    if id_eleve not in note:
        print("Cet élève n'a pas de notes enregistrées.")
        return
    
    matiere = input("Entrez la matière de la note à modifier: ")
    if matiere not in note[id_eleve]:
        print("Cette matière n'a pas de note enregistrée.")
        return
    
    nouvelle_note = input("Entrez la nouvelle note: ")
    note[id_eleve][matiere] = nouvelle_note
    print("Note modifiée.")
#supprimer une note
def supprimer_note():
    id_eleve = input("Entrez l'identifiant unique de l'élève: ")
    if id_eleve not in note:
        print("Cet élève n'a pas de notes enregistrées.")
        return
    
    matiere = input("Entrez la matière de la note à supprimer: ")
    if matiere not in note[id_eleve]:
        print("Cette matière n'a pas de note enregistrée.")
        return
    
    del note[id_eleve][matiere]
    if not note[id_eleve]:
        del note[id_eleve]
    print("Note supprimée.")

#afficher la note
def afficher_notes():
    id_eleve = input("Entrez l'identifiant unique de l'élève: ")
    if id_eleve not in note:
        print("Cet élève n'a pas de notes enregistrées.")
        return
    
    print(f"\nNotes de l'élève {id_eleve}:")
    for matiere, note in note[id_eleve].items():
        print(f"Matière: {matiere}, Note: {note}")

def main():
    start_time = time.time()
    
    while True:
        afficher_menu()
        choix = input("Choisissez une option: ")
        
        if choix == '1':
            ajouter_eleve()
        elif choix == '2':
            # Fonction de suppression d'élève à implémenter
            pass
        elif choix == '3':
            modifier_eleve()
        elif choix == '4':
            lister_eleves()
        elif choix == '5':
            print("\nGérer les notes:")
            print("1. Ajouter une note")
            print("2. Modifier une note")
            print("3. Supprimer une note")
            print("4. Afficher les notes")
            print("5. Retour")
            print("6. Accueil")
            choix_notes = input("Choisissez une option: ")
            
            if choix_notes == '1':
                ajouter_note()
            elif choix_notes == '2':
                modifier_note()
            elif choix_notes == '3':
                supprimer_note()
            elif choix_notes == '4':
                afficher_notes()
            elif choix_notes == '5':
                continue
            elif choix_notes == '6':
                pass  # Retour à l'accueil

        elif choix == '6':
            end_time = time.time()
            duration = end_time - start_time
            print(f"\nMerci de nous accorder votre temps,Durée de la session: {duration:.2f} secondes.")
            break

if __name__ == "__main__":
    main()

                      
        
        
        
