import requests

url = 'https://pokemondb.net/pokedex/all'
page = requests.get(url)

status = page.status_code

print(f"Status Code: {status}")

page.status_code == requests.codes.ok #Verifica se o code é 4XX client error ou 5XX server error response
    #condição


