def dict_tuple (S):
    A = []
    D = []
    if S != []:
        for x in S:
            count = S.count(x)
            if (x not in A):
                A.append(x)
                D.append((x,count))
        import operator
        D.sort()
        D.sort(key=operator.itemgetter(1),reverse = True)
        return D
    else:
        return ">> Your string is empty."
    return D
print (dict_tuple(["hello","world","welcome"]))

