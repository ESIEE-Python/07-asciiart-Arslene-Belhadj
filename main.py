"""Imports et définition des variables globales"""
import sys
sys.setrecursionlimit(1100)

#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en 
    argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici
    tableau = []
    compteur = 1
    if len(s)==0:
        return tableau
    for i in range (1, len(s)) :
        if s[i-1]==s[i]:
            compteur +=1
        else :
            tableau.append((s[i-1],compteur))
            compteur = 1
    tableau.append((s[i],compteur))
    return tableau



def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument 
    selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici

    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif
    tableau = []
    compteur = 1
    if len(s)==0:
        return tableau
    while compteur < len(s) and s[compteur] == s[0]:
        compteur += 1
    tableau.append((s[0],compteur))
    return tableau + artcode_r(s[compteur:])


#### Fonction principale###


def main():
    """Fonction main permettant le bon fonctionnement du code"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
