def salutations(nom: str):
    return f"Bonjour {nom}."

def age(annee_naissance: int):
    from datetime import date
    annee_actuelle = date.today().year
    return f"Votre âge est {annee_actuelle - annee_naissance} ans." 