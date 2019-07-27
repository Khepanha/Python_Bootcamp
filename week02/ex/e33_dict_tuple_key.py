def dict_tuple_key (S):
    A = []
    D = []
    if S != []:
        for x in S:
            count = S.count(x)
            if (x not in A):
                A.append (x)
                D.append ((x,count))
        D.sort()
        return D
    else:
        return ">> Your string is empty."
    return D
print (dict_tuple_key([]))
