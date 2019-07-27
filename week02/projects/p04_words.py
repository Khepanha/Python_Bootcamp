import collections
import re
def top_words(text):
    text = re.findall(r"[a-z]+['’]?[a-z]*", text.lower())
    x = dict(collections.Counter(text).most_common(3))
    return list(x.keys())
print (top_words(""))
