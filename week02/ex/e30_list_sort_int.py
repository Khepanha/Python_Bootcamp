def list_sort_int (L):
    A = []
    B = []
    for x in (L):
        try:
            A.append (int(x))
        except Exception:
            A.append (x)
    for x in (A):
        if type(x) == type(1):
            B.append(x)
    B.sort()
    return B
print (list_sort_int ([]))
