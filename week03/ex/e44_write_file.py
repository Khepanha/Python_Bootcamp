import os
def write_file(Filename,content):
    if (os.path.isfile(Filename)==False):
        f = open (Filename, 'w')
        f.write(content)
        return 1
        f.close()
    else:
        cont = input("Are you sure you want to replace " + (Filename) + "? [Y/N] \n")
        while cont.lower() != "y" and cont.lower() != "n":
            print ("Invalid Option")
            cont = input("Are you sure you want to replace " + (Filename) + "? [Y/N] \n")
        if (cont == "y" or cont == "Y"):
            f = open (Filename, 'w')
            f.write(content)
            return 1
        else:
            return 0
print (write_file())
    

