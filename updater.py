import requests

print('Checking for Updates...')

url = 'https://raw.githubusercontent.com/TitanWolfGamer/auto-holder/main/holder.py'

newest_update: str = requests.get(url).text

with open('./holder.py', 'r') as f:
    current_version: str = f.read()

has_newest_update: bool = newest_update == current_version

if not has_newest_update:
    print('Update found.')
    print('Installing Update...')

    with open('./holder.py', 'w') as f:
        f.write(newest_update)

    print('Update installed.')
else:
    print('Already at the newest version.')
