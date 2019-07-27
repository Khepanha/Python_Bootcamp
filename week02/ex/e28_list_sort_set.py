def list_sort_set (L):
    A = []
    L.sort()
    rev = L[::-1]
    for i in (rev):
        if i not in A:
            A.append(i)
    return A
print (list_sort_set([]))
