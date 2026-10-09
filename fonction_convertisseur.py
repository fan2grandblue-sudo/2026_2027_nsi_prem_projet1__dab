from math import floor

def converter ():
    nb50 = 0 # nombre de billets qui se trouveront dans la conversion
    nb20 = 0
    nb10 = 0
    nb5 = 0
    nb2 = 0
    nb1 = 0
    amount = int(input("\n\nHow much do you want to withdraw ? ")) # demande au user de rentrer la somme d'argent qu'il veut convertir en billets et pièces

    
    while amount <= 0 : # le programme redemande de rentrer un montant tant que celui-ci n'est pas compris entre 1 et 1000
        print ("\n\nThe amount must be between 1 and 1000.")
        amount = int(input("How much do you want to withdraw ? "))
    while amount > 1000 :
        print ("\n\nThe amount must be between 1 and 1000.")
        amount = int(input("How much do you want to withdraw ? "))
    while amount is float : # le programme redemande de rentrer un montant tant que celui-ci n'est pas un entier
        print ("\n\nThe amount must be an integer.")
        amount = int(input("How much do you want to withdraw ? "))
        
    
    for i in range (floor(amount / 50 )) : # permet de soustraire un nombre de billets de 50 € dépendant du montant
        nb50 = nb50 + 1 # ajoute 1 au nombre de billets de 50 € dans la conversion
        amount = amount - 50 # soustrait 50 au montant pour ne pas compter deux fois le même billet
    for i in range (floor(amount / 20 )) :
        nb20 = nb20 + 1 
        amount = amount - 20
    for i in range (floor(amount / 10 )) :
        nb10 = nb10 + 1 
        amount = amount - 10
    for i in range (floor(amount / 5 )) :
        nb5 = nb5 + 1 
        amount = amount - 5
    for i in range (floor(amount / 2 )) :
        nb2 = nb2 + 1 
        amount = amount - 2
    for i in range (floor(amount / 1 )) :
        nb1 = nb1 + 1 
        amount = amount - 1


    print ("\nHere is your change :\n")

    if nb50 == 1 :
        print ("1 bill of 50 €") # pour faire en sorte que ça affiche "billet" sans "s" puisque qu'il n'y en a qu'un seul
    elif nb50 > 1 :
        print (f"{nb50} bills of 50 €") # pour faire en sorte de ne pas afficher de billets rendus s'il n'y en a pas
    if nb20 == 1 :
        print ("1 bill of 20 €")
    elif nb20 > 1 :
        print (f"{nb20} bills of 20 €")
    if nb10 == 1 :
        print ("1 bill of 10 €")
    elif nb10 > 1 :
        print (f"{nb10} bills of 10 €")
    if nb5 == 1 :
        print ("1 bill of 5 €")
    elif nb5 > 1 :
        print (f"{nb5} bills of 5 €")
    if nb2 == 1 :
        print ("1 coin of 2 €")
    elif nb2 > 1 :
        print (f"{nb2} coins of 2 €")
    if nb1 == 1 :
        print ("1 coin of 1 €")
    elif nb1 > 1 :
        print (f"{nb1} coins of 1 €")

    print ("\n") # pour une question d'esthétique, afin de ne pas coller le texte à la suite de la conversion

    
    

converter ()