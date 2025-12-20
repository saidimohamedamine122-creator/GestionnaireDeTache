from Storage import ChargerTaches
from Tache import (
    AjouterTaches,
    AfficherTaches,
    MarquerTerminer,
    TachesTerminees,
    SupprimerTache
)

def Main():
    taches = ChargerTaches()

    while True:
        print("\n=== GESTIONNAIRE DE TÂCHES ===")
        print("1. Ajouter")
        print("2. Voir")
        print("3. Terminer")
        print("4. Voir terminées")
        print("5. Supprimer")
        print("6. Quitter")

        try:
            choix = int(input("Choix : "))
            if choix == 1:
                AjouterTaches(taches)
            elif choix == 2:
                AfficherTaches(taches)
            elif choix == 3:
                MarquerTerminer(taches)
            elif choix == 4:
                TachesTerminees(taches)
            elif choix == 5:
                SupprimerTache(taches)
            elif choix == 6:
                print("👋 Bye")
                break
            else:
                print("Choix invalide")
        except ValueError:
            print("Entrée invalide")

if __name__ == "__main__":
    Main()
