def add_user ():
    pass



def register ():
    register = input ("Register : ")
    if register in excel.group:
        pin ()
    else:
        print ("Account doesn't exist")

    




def pin ():
    PIN = int (input ("Enter PIN : "))
    while count_false<=3:
        if PIN == PIN_user:
            open_folder ()
        else:
            count_false +=1
    break