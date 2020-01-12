import random #importe la fonction random
def course(): #definit une fonction
    '''génère une course aléatoirement
    '''
    course=[] #crée une liste vide
    while len(course)!=5: #tant que la liste ne comporte pas 5 éléments
        a=random.randint(1,16) #genere un nombre
        if a not in course: #si le nombre n'est pas dans la liste
            course.append(a) #on l'ajoute

    return course

def pari():
    '''le joueur rentre son pari
    '''
    pari=[] #crée une liste vide
    position=1 #la postion dans la liste est toujours décalée de 1. Cette variable affiche la position "véritable" à l'utilisateur
    while len(pari)!=5:
        numero=int(input("Quel cheval va arriver en position numéro " +str(position)+"? ")) #demande le numéro du cheval
        while numero in pari or 16<numero or numero<1:
            numero=int(input("Ce Cheval est déjà rentré soit le numéro est trop grand ou trop petit. Rentrez le cheval pour la position "+str(position)+" ")) #si le numéro est déjà rentré ou n'est pas compris entre 1 et 16, il le redemande
        if numero not in pari: # si le numéro n'est pas rentré
            pari.append(numero) #il est ajouté à la liste
            position=position+1 #on ajoute 1 a position pour que l'utilisateur ne se trompe pas lors de la saisie
    return pari

def quinte (course,pari):
    '''vérifie si le pari est un quinté
    '''
    ordre=0
    for i in range(0,5): #si les numéros sont identiques, on rajoute 1 à ordre
        if course[i]==pari[i]: #vérifie que tous les numéros sont identiques
            ordre=ordre+1
    if ordre==5: #si tout les numéros sont identiques, on renvoie le gain en str pour l'afficher directement
        return "Ordre"
    else:
        return False #sinon , on renvoie false afin de lancer la fonction ordre

def ordre (course,pari):
    '''verifie si le pari est un desordre, bonus 4 ou bonus 3
    '''
    ordre=0
    for i in range (0,5): #i prend succesivement des valeurs allant de 0 à 5
        if course[i] in pari: #si le numéro est dans le 2 listes, on ajoute 1 à ordre
            ordre=ordre+1
    
    if ordre==5: #si ordre ==5, on a un quinté dans le désordre
        return "Désordre"
    
    elif ordre==4: #ensuite, on se refere au document PMU pour determiner le gain. Ordre est egal au nombre de numéros justes.
        return "Bonus 4"

    elif ordre==3:
        return "Bonus 3"
    
    else:
        return "Perdu"



arrivée=course() #on détermine la course aléatoirement
print(arrivée)
pari=pari() #on demande le pari du joeur
gain=quinte(arrivée,pari) #on regarde si le joeur a obtenu un quinté
if gain==False: #si on a pas de quinté, on teste les autres gains
    gain= ordre(arrivée,pari)

print("Votre gain est", gain) #on indique le gain au joueur


