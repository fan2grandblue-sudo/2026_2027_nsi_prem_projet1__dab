from math import floor


def convertisseur ():
    nb50 = 0 # nombre de billets qui se trouveront dans la conversion
    nb20 = 0
    nb10 = 0
    nb5 = 0
    nb2 = 0
    nb1 = 0
    monnaie = []
    montant = int(input("Quel montant veux-tu prélever ? ")) # demande au user de rentrer la somme d'argent qu'il veut convertir en billets et pièces
    
    for i in range (floor(montant / 50 )) : # permet de soustraire un nombre de billets de 50 € dépendant du montant
        nb50 = nb50 + 1 # ajoute 1 au nombre de billets de 50 € dans la conversion
        montant = montant - 50
    monnaie.append(nb50)
    for i in range (floor(montant / 20 )) :
        nb20 = nb20 + 1 
        montant = montant - 20
    monnaie.append(nb20)
    for i in range (floor(montant / 10 )) :
        nb10 = nb10 + 1 
        montant = montant - 10
    monnaie.append(nb10)
    for i in range (floor(montant / 5 )) :
        nb5 = nb5 + 1 
        montant = montant - 5
    monnaie.append(nb5)
    for i in range (floor(montant / 2 )) :
        nb2 = nb2 + 1 
        montant = montant - 2
    monnaie.append(nb2)
    for i in range (floor(montant / 1 )) :
        nb1 = nb1 + 1 
        montant = montant - 1
    monnaie.append(nb1)
    
    print (f"\nCela vous donne :\n\n{nb50} billet(s) de 50€. \n{nb20} billet(s) de 20€. \n{nb10} billet(s) de 10€. \n{nb5} billet(s) de 5€. \n{nb2} pièce(s) de 2€. \n{nb1} pièce(s) de 1€. ")

    #return monnaie

print (convertisseur ())
