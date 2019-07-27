import re
def regex_html (S):
    r = re.sub(r'<.*?>','',S)
    return r
print (regex_html())

