def array_split(A):
    B = []
    if A != []:
        for x in A:
            a = list(x)
            B.append(a)
        return B
    else:
        return (">> []")
print (array_split ([]))
