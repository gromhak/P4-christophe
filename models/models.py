import json
import os
import random
import datetime


class Joueurs :
    def liste_joueur_JSON():
        # On crée le dossier JSON pour stocker les BDD s'il n'existe pas
        os.makedirs("JSON", exist_ok=True)
        bdd_joueurs = "JSON/joueurs.json"
        if os.path.exists(bdd_joueurs):
            # Si le fichier JSON pour les joueurs existe, on récupère la liste des joueurs
            with open(bdd_joueurs, 'r') as f:
                contenu = json.load(f)
        else :
            contenu = "ERR01"
        return contenu

class Joueur :
    def __init__(self, identifiant_national, nom_joueur, prenom_joueur, sexe, date_naissance, tournoi_en_cours,
                 tour_en_cours, score_actuel = 0):
        self.identifiant_national = identifiant_national
        self.nom_joueur = nom_joueur
        self.prenom_joueur = prenom_joueur
        self.sexe = sexe
        self.date_naissance = date_naissance
        self.tournoi_en_cours = tour_en_cours
        self.score_actuel = score_actuel


class Tournoi :
    def __init__(self, nom_tournoi, lieu_tournoi, remarque_tournoi, debut_tournoi, fin_tournoi, nb_tours, liste_tours,
                 liste_joueurs, tour_en_cours = " ", gagnant = " " ):
        self.nom_tournoi = nom_tournoi
        self.lieu_tournoi = lieu_tournoi
        self.remarque_tournoi = remarque_tournoi
        self.debut_tournoi = debut_tournoi
        self.fin_tournoi = fin_tournoi
        self.nb_tours = nb_tours
        self.liste_tours = liste_tours
        self.liste_joueurs = liste_joueurs
        self.tour_en_cour = tour_en_cours
        self.gagnant = gagnant


class Tour :
    def __init__(self, liste_joueurs, nb_match, liste_matchs, date_debut_tour, date_fin_tour):
        pass


class Match :
    def __init__(self, joueur_blanc =" ", joueur_noir = " ", score_JB = 0, score_JN = 0, gagnant = null):
        pass


if __name__ == "__main__":
    print("Merci de commencer par lancer main.py")
