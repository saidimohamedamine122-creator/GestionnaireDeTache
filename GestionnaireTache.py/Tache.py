from Storage import SauvegarderTaches

def AjouterTaches(taches):
    description = input("📝 Description de la tâche : ")
    print("Priorité : 1. Haute / 2. Moyenne / 3. Basse")

    try:
        priorite = int(input("Choix : "))
        if priorite not in [1, 2, 3]:
            priorite = 2
    except ValueError:
        priorite = 2

    nouvel_id = max([t["id"] for t in taches], default=0) + 1

    nouvelle_tache = {
        "id": nouvel_id,
        "description": description,
        "termine": False,
        "priorité": priorite
    }

    taches.append(nouvelle_tache)
    SauvegarderTaches(taches)
    print("✅ Tâche ajoutée")

def AfficherTaches(taches):
    if not taches:
        print("📭 Aucune tâche")
        return

    priorite_nom = {1: "Haute", 2: "Moyenne", 3: "Basse"}
    taches_triees = sorted(taches, key=lambda t: t["priorité"])

    for t in taches_triees:
        etat = "✅" if t["termine"] else "❌"
        print(f"[{etat}] ID:{t['id']} | {t['description']} | {priorite_nom[t['priorité']]}")

def MarquerTerminer(taches):
    AfficherTaches(taches)
    try:
        id_tache = int(input("ID à terminer : "))
        for t in taches:
            if t["id"] == id_tache:
                t["termine"] = True
                SauvegarderTaches(taches)
                print("✅ Terminée")
                return
        print("❌ ID introuvable")
    except ValueError:
        print("❌ Entrée invalide")

def TachesTerminees(taches):
    terminees = [t for t in taches if t["termine"]]
    if not terminees:
        print("Aucune tâche terminée")
        return
    for t in terminees:
        print(f"[✓] {t['id']} - {t['description']}")

def SupprimerTache(taches):
    AfficherTaches(taches)
    try:
        id_tache = int(input("ID à supprimer : "))
        for i, t in enumerate(taches):
            if t["id"] == id_tache:
                taches.pop(i)
                SauvegarderTaches(taches)
                print("🗑️ Supprimée")
                return
        print("❌ ID introuvable")
    except ValueError:
        print("❌ Entrée invalide")
