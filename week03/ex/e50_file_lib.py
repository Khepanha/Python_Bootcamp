import os
import shutil
class myclass:
    def current_path(F):
        return F
    print (current_path(os.getcwd()))
    def current_files (F):
        A = []
        B = []
        for subdir, dirs, files in F:
            A.append ((dirs,files))
        for x in A:
            for i in x:
                for j in i:
                    if os.path.isdir(j):
                        B.append ((j,"Folder"))
                        B.sort()
                    if os.path.isfile(j):
                        B.append ((j,"File"))
                        B.sort()
        return B
    print (current_files(os.walk('./')))
    def read_file(F):
        try:
            f = open(F, 'r')
            return (f.read())
            f.close()
        except:
            return "Invalid Filename"
    print (read_file("e43_read_file.py"))
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
    print (write_file("test_3.txt","Bonjour kdor Chmar"))

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
    print (create_folder(["Folder1", "Folder2", "Folder3"]))
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
    print (delete_file("test_2.txt"))











        

    
