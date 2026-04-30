import os
from time import time
from tkinter.filedialog import askdirectory
import json

TEMP_FILENAME: str = f'AutoHolder-{time()}'

def get_installation_directory() -> str:
    return askdirectory(title='Select Folder for installation')

def set_up_config(installation_directory: str) -> dict:
    return {'path': installation_directory}


def install_program(installation_directory: str, temp_filename: str) -> None:
    temp_dir: str = os.environ['TEMP']
    temp_path: str = rf'{temp_dir}\{temp_filename}'

    config_content: dict = set_up_config(installation_directory)

    os.system(f'git clone https://github.com/TitanWolfGamer/auto-holder.git {temp_path}')
    os.remove(fr'{temp_path}\installer.py')
    os.remove(fr'{temp_path}\.gitignore')

    # overwriting default config data
    with open(fr'{temp_path}\config.json', 'w') as f:
        json.dump(config_content, f)


install_program(get_installation_directory(), TEMP_FILENAME)