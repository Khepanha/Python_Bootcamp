def list_sort_str (S):
    A = []
    for x in S:
        if (type(x) != type(1) and x.isdigit() == False):
            x = x.replace("-","")
        if (type(x) != type(1) and x.isdigit() == False):
            A.append(x)
    return A
print (list_sort_str(['abc', 'def', -1, 2, 3, '-123', '888', 'hello']))

