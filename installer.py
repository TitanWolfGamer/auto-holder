import os
from time import time
from tkinter.filedialog import askdirectory

class Program:
    def __init__(self) -> None:
        self.__inst_dir: str = askdirectory(title='Select Folder for installation')

    def install(self, temp_filename: str = f'AutoHolder-{time()}') -> None:
        temp_dir: str = os.environ['TEMP']
        temp_path: str = rf'{temp_dir}\{temp_filename}'

        os.system(f'git clone https://github.com/TitanWolfGamer/auto-holder.git {temp_path}')
        os.remove(fr'{temp_path}\installer.py')
        os.remove(fr'{temp_path}\.gitignore')

        os.rename(temp_path, fr'{self.__inst_dir}\AutoHolder')

program: Program = Program()
program.install()
