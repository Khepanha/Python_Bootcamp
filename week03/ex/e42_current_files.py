import os
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
