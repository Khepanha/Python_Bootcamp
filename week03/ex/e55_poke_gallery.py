import requests
def poke_gallery (poke):
    a = []
    b = []
    url = 'https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json'
    r = requests.get(url)
    s = r.json().get('pokemon')
    if poke != [] and poke != '':
        for i in s:
            k = 0
            t = i.get('type')
            for j in poke:
                if j in t:
                    k += 1
            if k == len(poke):
                u = i.get('img')
                a.append(u)
        for l in a:
            style = "<img src = " + l + " height = '100px' width = '100px'>"
            f = open('pokemon.html', 'a')
            f.write(style)
            f.close()
        return a
    if poke == [] or poke == '':
        for img in s:
            w = img.get('img')
            b.append(w)
        for l in b:
            style = "<img src = " + l + " height = '100px' width = '100px'>"
            f = open('pokemon.html', 'a')
            f.write(style)
            f.close()
    return b
print (poke_gallery(''))