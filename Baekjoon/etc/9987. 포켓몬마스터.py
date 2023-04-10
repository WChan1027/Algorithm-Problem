from bs4 import BeautifulSoup
import requests

html = requests.get("http://web.archive.org/web/20140301191716/http://pokemondb.net/pokedex/national")
html = html.content
soup = BeautifulSoup(html, "html.parser")

idx = int(input())

card = soup.select("span.infocard-tall")[idx-1]
name = str(card.select("a.ent-name"))
types = card.select("a.itype")

pokemon_name = ""
start = 0
for word in name:
    if start == 1 and word == '<':
        break
    
    if start == 1:
        pokemon_name += word

    if word == '>':
        start = 1

print(pokemon_name)

pokemon_type = []
for case in types:
    type_form = str(case)
    type = ""
    start = 0
    for word in type_form:
        if start == 1 and word == '<':
            break

        if start == 1:
            type += word

        if word == '>':
            start = 1
    
    pokemon_type.append(type)

print(*pokemon_type)