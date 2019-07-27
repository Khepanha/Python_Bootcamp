import requests
from datetime import datetime
def get_currencies (PAIR):
    A = []
    URL = 'https://freeforexapi.com/api/live'
    for c in PAIR:
        r = requests.post(url = URL, params = {'pairs': c })
        t = (r.json().get('rates').get(c).get('rate'))
        u = r.json().get('rates').get(c).get('timestamp')
        v = datetime.fromtimestamp(u)
        dt = v.strftime('%d/%m/%Y %H:%M')
        A.append((c,t,u,dt))
    return A
print (get_currencies ([]))


