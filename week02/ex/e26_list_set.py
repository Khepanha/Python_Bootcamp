def list_set (L):
    A = []
    for i in (L):
        if i not in A:
            A.append(i)
    return A
print (list_set([]))
