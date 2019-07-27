import re
def regex_urls(S):
    if S == '':
        return ''
    else:
        url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', S)
        return url
print (regex_urls())


