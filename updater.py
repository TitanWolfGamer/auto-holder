import requests

r = requests.get('https://api.github.com/repos/TitanWolfGamer/nimrod/contents/nimrod.py')

r2 = requests.get(r.json()['download_url'])

print(r2.content.decode())