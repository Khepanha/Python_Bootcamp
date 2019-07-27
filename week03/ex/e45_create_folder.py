import os
import shutil
def create_folder(Folder):
    i = 0
    for F in Folder:
        if (os.path.isdir(F) == False):
            os.mkdir(F)
        else:
            I = input ("Are you sure you want to replace " + (F) + "? [Y/N] \n")
            while (I.lower() != "y" and I.lower() != "n"):
                print ("Invalid Option")
                I = input ("Are you sure you want to replace " + (F) + "? [Y/N] \n")           
            if (I == "y" or I == "Y"):
                i += 1
                shutil.rmtree (F)
                os.mkdir(F)              
            else:
                continue
    return i
print (create_folder([]))
