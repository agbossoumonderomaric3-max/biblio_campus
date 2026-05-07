import json
import os

FICHIER = "data/library.json"

def charger_donnees():
    if not os.path.exists(FICHIER):
        return {"livres": []}
    with open(FICHIER, "r", encoding="utf-8") as f:
        return json.load(f)

def sauvegarder_donnees(donnees):
    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump(donnees, f, indent=4, ensure_ascii=False)