import requests
def get_fbid(fb_url):
        URL = "https://findmyfbid.com/"
        try:
                r = requests.post(url=URL, params={'url': fb_url})
                return (r.status_code, r.json().get('id'))
        except:
                return (r.status_code, 0)
print (get_fbid (""))
