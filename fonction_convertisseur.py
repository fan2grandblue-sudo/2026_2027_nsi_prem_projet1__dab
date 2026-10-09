from math import floor

def convertisseur ():
    nb50 = 0 # nombre de billets qui se trouveront dans la conversion
    nb20 = 0
    nb10 = 0
    nb5 = 0
    nb2 = 0
    nb1 = 0
    montant = int(input("\n\nQuel montant (compris entre 1 et 1000) voulez-vous prélever ? ")) # demande au user de rentrer la somme d'argent qu'il veut convertir en billets et pièces

    
    while montant <= 0 : # le programme redemande de rentrer un montant tant que celui-ci n'est pas compris entre 1 et 1000
        print ("\n\nLe montant doit être compris entre 1 et 1000.")
        montant = int(input("Quel montant voulez-vous prélever ? "))
    while montant > 1000 :
        print ("\n\nLe montant doit être compris entre 1 et 1000.")
        montant = int(input("Quel montant voulez-vous prélever ? "))
    
    
    for i in range (floor(montant / 50 )) : # permet de soustraire un nombre de billets de 50 € dépendant du montant
        nb50 = nb50 + 1 # ajoute 1 au nombre de billets de 50 € dans la conversion
        montant = montant - 50 # soustrait 50 au montant pour ne pas compter deux fois le même billet
    for i in range (floor(montant / 20 )) :
        nb20 = nb20 + 1 
        montant = montant - 20
    for i in range (floor(montant / 10 )) :
        nb10 = nb10 + 1 
        montant = montant - 10
    for i in range (floor(montant / 5 )) :
        nb5 = nb5 + 1 
        montant = montant - 5
    for i in range (floor(montant / 2 )) :
        nb2 = nb2 + 1 
        montant = montant - 2
    for i in range (floor(montant / 1 )) :
        nb1 = nb1 + 1 
        montant = montant - 1


    print ("\nVoici votre monnaie :\n")

    if nb50 == 1 :
        print ("1 billet de 50 €") # pour faire en sorte que ça affiche "billet" sans "s" puisque qu'il n'y en a qu'un seul
    elif nb50 > 1 :
        print (f"{nb50} billets de 50 €") # pour faire en sorte de ne pas afficher de billets rendus s'il n'y en a pas
    if nb20 == 1 :
        print ("1 billet de 20 €")
    elif nb20 > 1 :
        print (f"{nb20} billets de 20 €")
    if nb10 == 1 :
        print ("1 billet de 10 €")
    elif nb10 > 1 :
        print (f"{nb10} billets de 10 €")
    if nb5 == 1 :
        print ("1 billet de 5 €")
    elif nb5 > 1 :
        print (f"{nb5} billets de 5 €")
    if nb2 == 1 :
        print ("1 pièce de 2 €")
    elif nb2 > 1 :
        print (f"{nb2} pièces de 2 €")
    if nb1 == 1 :
        print ("1 pièce de 1 €")
    elif nb1 > 1 :
        print (f"{nb1} pièces de 1 €")

    
    

convertisseur ()