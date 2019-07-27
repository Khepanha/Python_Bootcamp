import re
def regex_word (First, Second):
    shortword = re.compile(r'\W*\b\w{1,' + re.escape(str(First)) + r'}\b')
    return shortword.sub('', Second)
print (regex_word())
