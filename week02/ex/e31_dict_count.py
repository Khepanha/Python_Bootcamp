def dict_count (S):
    A = []
    D = {}
    S = sorted(S)
    for x in S:
        count = S.count(x)
        if (x not in A):
            A.append(x)
            D.update({x:count})
    return D
print (dict_count (["hello","world","welcome"]))


















