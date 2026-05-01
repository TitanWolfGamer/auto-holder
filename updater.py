import requests
import base64

def check_for_updates() -> None:
    print('Checking for Updates...')

    url = 'https://api.github.com/repos/TitanWolfGamer/auto-holder/contents/holder.py?ref=main'

    newest_update_data: dict = requests.get(url).json()
    newest_update: str = base64.b64decode(newest_update_data['content']).decode('utf-8')

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

def main() -> None:
    check_for_updates()

if __name__ == '__main__':
    main()