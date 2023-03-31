import sys
import json

class MenuPrincipal :
    #On crée une classe pour appeler le menu principal quand on le souhaite

    def __init__(self):
        self.code_menu_principal = 0
    def menuprincipal(self) :
        #On fait une boucle pour que le menu s'affiche tant que l'utilisateur ne donne pas une réponse autorisée
        while self.code_menu_principal != 1 and self.code_menu_principal != 2 and self.code_menu_principal != 3 and self.code_menu_principal != 4 :
            print("*" *66)
            print("-" * 66)
            print("Bienvenue dans le menu principal, merci de faire votre sélection :")
            print("-" *66)
            print(" ")
            print("1. Commencer un nouveau tournoi")
            print("2. Consulter un ancien tournoi")
            print("3. Consulter la liste des joueurs enregistrés")
            print("4. quitter le programme")
            print(" ")
            print("*" *66)
            menu_principal = input("Votre réponse :")
            if menu_principal.isdigit() :
                self.code_menu_principal = int(menu_principal)
            else :
                self.code_menu_principal = 0
                print(" ")
                print("Merci de choisir parmis les options 1, 2, 3 ou 4")
                print(" ")
            if self.code_menu_principal != 0 and self.code_menu_principal != 1 and self.code_menu_principal != 2 and self.code_menu_principal != 3 and self.code_menu_principal != 4 :
                print(" ")
                print("Merci de choisir parmis les options 1, 2, 3  ou 4")
                print(" ")
        return self.code_menu_principal

class MenuNouveauTournoi :
    pass

class MenuConsulterTournoi :
    pass

class MenuConsulterListeJoueur :
    def __init__(self):
        self.code_menu_joueur = 0
    def menujoueur(self):
        while self.code_menu_joueur != 1 and self.code_menu_joueur != 2 and self.code_menu_joueur != 3 and self.code_menu_joueur != 4 and self.code_menu_joueur != 5 :
            print("*" *66)
            print("-" * 66)
            print("Bienvenue dans le menu de gestion des joueur, merci de faire votre sélection :")
            print("-" *66)
            print(" ")
            print("1. Consulter la liste des joueurs enregistrés")
            print("2. Consulter les informations d'un joueur")
            print("3. Créer un nouveau joueur")
            print("4. Supprimer un joueur")
            print("5. Retour au menu principal")
            print(" ")
            print("*" *66)
            menu_joueur = input("Votre réponse :")
            if menu_joueur.isdigit() :
                self.code_menu_joueur = int(menu_joueur)
            else :
                self.code_menu_joueur = 0
                print(" ")
                print("Merci de choisir parmis les options 1, 2, 3, 4 ou 5")
                print(" ")
            if self.code_menu_joueur != 0 and self.code_menu_joueur != 1 and self.code_menu_joueur != 2 and self.code_menu_joueur != 3 and self.code_menu_joueur != 4 and self.code_menu_joueur !=5 :
                print(" ")
                print("Merci de choisir parmis les options 1, 2, 3, 4  ou 5")
                print(" ")
        return self.code_menu_joueur

class FormulaireNouveauJoueur :

    def questionnaire():
        identifiant = input("Quel est votre identifiant national ?")
        nom = input("Quel est votre nom ?")
        prenom = input("Quel est votre prénom ?")
        sexe = input("Êtes vous un homme ou une femme ?")
        date_naissance = input("Quelle est votre date de naissance ?")
        remarque = " "
        liste_tournois = 0
        moyenne_points = 0
        reponses_formulaire = [identifiant, nom, prenom, sexe, date_naissance, remarque, liste_tournois, moyenne_points]
        return reponses_formulaire

class FormulaireRechercheJoueur :
    def questionnaire():
        identifiant = input("Quel est l'identifiant national du joueur ?")
        return identifiant
    def affichage(resultat):
        print("Voici les informations demandées")
        for cle in resultat :
            print(cle, ":", resultat[cle])

if __name__ == "__main__":
    print("Merci de commencer par lancer main.py")