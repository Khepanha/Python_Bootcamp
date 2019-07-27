import re
def regex_alpha_k (check):
    if (check == ''):
        return False
    x = re.findall("[a-kA-K0-5]", check)
    s = list(check)
    if (x == s):
        return True
    else:
        return False
print (regex_alpha_k())
