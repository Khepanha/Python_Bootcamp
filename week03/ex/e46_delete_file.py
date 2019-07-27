import os
def delete_file (F):
    if (os.path.isdir(F) == True):
        I = input ("Are you sure you want to delete " + (F) + "? [Y/N] \n")
        while (I.lower() != "y" and I.lower() != "n"):
            print ("Invalid Option")
            I = input ("Are you sure you want to delete " + (F)+ "? [Y/N] \n")
        if (I == "y" or I == "Y"):
            os.rmdir(F)
            return 1
        else:
           return 0
    if (os.path.isfile(F) == True):
        I = input ("Are you sure you wnat to delete " + (F) + "? [Y/N] \n")
        while (I.lower() != "y" and I.lower() != "n"):
            print ("Invalid Option")
            I = input ("Are you sure you want to delete " + (F) + "? [Y/N] \n")
        if (I == "Y" or I == "y"):
            os.remove(F)
            return 1
        else:
            return 0
    else:
        return 0
print (delete_file())
