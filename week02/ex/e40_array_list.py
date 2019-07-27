def array_list(L):
    A = []
    if (L != []):
        for x in L:
            if (x not in A):
                A.append (x)
        return A
    else:
        return (">> []")
print (array_list([]))
