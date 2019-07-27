import re
def regex_par(S):
    r = re.sub(r'\([^)]*\)', '',S)
    return r
print (regex_par())
