import requests
def get_html (url):
    r = requests.get(url)
    return r.content
print (get_html("https://en.wikipedia.org/wiki/Fox_Glacier"))
    

