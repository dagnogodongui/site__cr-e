
while True:
                print("1: Ajouter un professeur")
                print("2: Supprimer un professeur")
                print("3: Modifier les informations du professeur")
                print("4: Lister les professurs")
                print("5: Obtenier le dernier professeur ajouté")
                print("6: Retour")
                print("0: Accueil")












def main_menu():
    while True:
        print("\nMenu Principal")
        print("1: Gestion des Professeurs")
        print("0: Quitter")

        choix = input("Entrez votre choix: ")

        if choix == '1':
            professeur_menu()
        elif choix == '0':
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

def professeur_menu():
    while True:
        print("\nMenu des ")
        print("1: Ajouter un professeur")
        print("2: Supprimer un professeur")
        print("3: Modifier les informations du professeur")
        print("4: Lister les professeurs")
        print("5: Obtenir le dernier professeur ajouté")
        print("6: Retour")

        choix = input("Entrez votre choix: ")

        if choix == '1':
            ajouter_professeur()
        elif choix == '2':
            supprimer_professeur()
        elif choix == '3':
            modifier_professeur()
        elif choix == '4':
            lister_professeurs()
        elif choix == '5':
            obtenir_dernier_professeur()
        elif choix == '6':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

def ajouter_professeur():
    print("Ajout d'un professeur...")

def supprimer_professeur():
    print("Suppression d'un professeur...")

def modifier_professeur():
    print("Modification des informations du professeur...")

def lister_professeurs():
    print("Liste des professeurs...")

def obtenir_dernier_professeur():
    print("Obtention du dernier professeur ajouté...")

# Démarrage du programme
if __name__ == "__main__":
    main_menu()
    
    
 
 