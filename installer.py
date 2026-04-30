import os

from tkinter.filedialog import askdirectory

def get_installation_directory() -> str:
    return askdirectory(title='Select Folder for installation')

def set_up_config(installation_directory: str) -> dict:
    return {'path': installation_directory}


def install_program(installation_directory: str) -> None:
    os.system('git clone ')