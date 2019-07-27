import requests
def poke_type (Poke):
    A = []
    URL = 'https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json'
    g = requests.get(URL)
    e = g.json().get('pokemon')
    for i in e:
        k = 0
        t = i.get('type')
        for j in Poke:
            if (j in t):
                k += 1
                u = i.get('name')
                v = i.get('id')
        if (k == len(Poke)):
            A.append((v,u))
    return A
print (poke_type ([]))
