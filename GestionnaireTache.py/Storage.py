import json
import os

FICHIER = "taches.json"

def ChargerTaches():
    if not os.path.exists(FICHIER):
        return []

    try:
        with open(FICHIER, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except json.JSONDecodeError:
        return []

def SauvegarderTaches(taches):
    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump(taches, f, indent=4, ensure_ascii=False)
