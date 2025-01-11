import math


#données représentées sous forme de liste de dictionnaires
data = [
    {"Ciel": "soleil", "Température": "chaud", "Humidité": "élevée", "Vent": "faible", "Jouer au Tennis": "non"},
    {"Ciel": "soleil", "Température": "chaud", "Humidité": "élevée", "Vent": "fort", "Jouer au Tennis": "non"},
    {"Ciel": "couvert", "Température": "chaud", "Humidité": "élevée", "Vent": "faible", "Jouer au Tennis": "oui"},
    {"Ciel": "pluie", "Température": "doux", "Humidité": "élevée", "Vent": "faible", "Jouer au Tennis": "oui"},
    {"Ciel": "pluie", "Température": "froid", "Humidité": "normale", "Vent": "faible", "Jouer au Tennis": "oui"},
    {"Ciel": "pluie", "Température": "froid", "Humidité": "normale", "Vent": "fort", "Jouer au Tennis": "non"},
    {"Ciel": "couvert", "Température": "froid", "Humidité": "normale", "Vent": "fort", "Jouer au Tennis": "oui"},
    {"Ciel": "soleil", "Température": "doux", "Humidité": "élevée", "Vent": "faible", "Jouer au Tennis": "non"},
    {"Ciel": "soleil", "Température": "froid", "Humidité": "normale", "Vent": "faible", "Jouer au Tennis": "oui"},
    {"Ciel": "pluie", "Température": "doux", "Humidité": "normale", "Vent": "faible", "Jouer au Tennis": "oui"},
    {"Ciel": "soleil", "Température": "doux", "Humidité": "normale", "Vent": "fort", "Jouer au Tennis": "oui"},
    {"Ciel": "couvert", "Température": "doux", "Humidité": "élevée", "Vent": "faible", "Jouer au Tennis": "oui"},
    {"Ciel": "couvert", "Température": "chaud", "Humidité": "normale", "Vent": "faible", "Jouer au Tennis": "oui"},
    {"Ciel": "pluie", "Température": "doux", "Humidité": "élevée", "Vent": "fort", "Jouer au Tennis": "non"}
]

def calculer_entropie(data, colonne_cible):
    # Compter les occurrences des classes dans la colonne cible
    frequences = {}
    for ligne in data:
        valeur = ligne[colonne_cible]
        if valeur in frequences:
            frequences[valeur] += 1
        else:
            frequences[valeur] = 1

    # Calculer la taille totale de l'ensemble
    total = len(data)

    # Calculer l'entropie
    entropie = 0
    for count in frequences.values():
        prob = count / total
        entropie -= prob * math.log2(prob)

    return entropie


# Calculer l'entropie pour "Jouer au Tennis"
entropie = calculer_entropie(data, "Jouer au Tennis")
print(f"Entropie de 'Jouer au Tennis' : {entropie:.3f} \n")





#Divise les données en sous-groupes selon les valeurs d'un attribut.
def diviser_par_attribut(data, colonne_attribut):
    sous_groupes = {}
    for ligne in data:
        valeur = ligne[colonne_attribut]
        if valeur not in sous_groupes:
            sous_groupes[valeur] = []
        sous_groupes[valeur].append(ligne)
    return sous_groupes


#Calcule l'entropie conditionnelle pour un attribut donné.
def calculer_entropie_conditionnelle(data, colonne_cible, colonne_attribut):
    sous_groupes = diviser_par_attribut(data, colonne_attribut)
    total = len(data)
    entropie_conditionnelle = 0

    for sous_ensemble in sous_groupes.values():
        poids = len(sous_ensemble) / total
        entropie_conditionnelle += poids * calculer_entropie(sous_ensemble, colonne_cible)

    return entropie_conditionnelle


#Calcule le gain d'information pour un attribut donné.
def calculer_gain(data, colonne_cible, colonne_attribut):
    entropie_totale = calculer_entropie(data, colonne_cible)
    entropie_conditionnelle = calculer_entropie_conditionnelle(data, colonne_cible, colonne_attribut)
    gain = entropie_totale - entropie_conditionnelle
    return gain



attributs = ["Ciel", "Température", "Humidité", "Vent"]
# Calcul des gains
for attribut in attributs:
    gain = calculer_gain(data, "Jouer au Tennis", attribut)
    print(f"Gain pour '{attribut}' : {gain:.3f}")





def selectionner_meilleur_attribut(data, colonne_cible, attributs):
    gains = {attribut: calculer_gain(data, colonne_cible, attribut) for attribut in attributs}
    meilleur_attribut = max(gains, key=gains.get)
    return meilleur_attribut

def construire_arbre(data, colonne_cible, attributs):
    #Si toutes les valeurs sont "oui" ou "non"
    classes = {ligne[colonne_cible] for ligne in data}
    if len(classes) == 1:
        return classes.pop()  # Retourne "oui" ou "non"
    
    # Si aucun attribut n'est disponible, retourner la classe majoritaire
    if not attributs:
        frequences = {valeur: sum(1 for ligne in data if ligne[colonne_cible] == valeur) for valeur in classes}
        return max(frequences, key=frequences.get)
    
    # Sélectionner le meilleur attribut
    meilleur_attribut = selectionner_meilleur_attribut(data, colonne_cible, attributs)
    
    # Étape 4 : Construire l'arbre récursivement
    arbre = {meilleur_attribut: {}}
    sous_groupes = diviser_par_attribut(data, meilleur_attribut)

    #parcourir chaque valeur de l'attribut sélectionné
    for valeur in sous_groupes:
        sous_ensemble = sous_groupes[valeur]  # récupérer les données associées à cette valeur
        sous_attributs = [attr for attr in attributs if attr != meilleur_attribut]  # Retirer le meilleur attribut
        sous_arbre = construire_arbre(sous_ensemble, colonne_cible, sous_attributs)  # Construire le sous-arbre
        arbre[meilleur_attribut][valeur] = sous_arbre  # Ajouter le sous-arbre à l'arbre principal
    
    return arbre




attributs = ["Ciel", "Température", "Humidité", "Vent"]
arbre = construire_arbre(data, "Jouer au Tennis", attributs)
print("Arbre de décision :", arbre)
