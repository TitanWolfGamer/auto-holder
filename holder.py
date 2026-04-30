import os, sys, time
from tkinter import Tk, Button, Label, Entry, OptionMenu, StringVar
import ctypes

try:
    import pyautogui
except ImportError:
    print('PyAutoGUI is not installed!')
    print("It's essential for the program to execute.")
    print('Install PyAutoGUI? [y/n]')
    if input('> ') == 'y':
        os.system('pip install pyautogui')
        print()
        print()
        print('Installing dependencies Complete. Rerun the application to start it.')
        input('[PRESS ENTER TO EXIT]')
        sys.exit()
    else:
        print('Bye :)')
        time.sleep(1)
        sys.exit()

import pyautogui as pag

root = Tk()

MOUSE_BTN: str = ''
SM_SWAPBUTTON = 23


def swapped_primary_button() -> bool:
    user32 = ctypes.WinDLL("user32", use_last_error=True)
    user32.GetSystemMetrics.restype = ctypes.c_int
    user32.GetSystemMetrics.argtypes = (ctypes.c_int,)

    swapped = user32.GetSystemMetrics(SM_SWAPBUTTON)
    return swapped != 0

def update_mouse_button(btn):
    global MOUSE_BTN
    MOUSE_BTN = btn

def start_app():
    # validate mouse button

    if not MOUSE_BTN:
        error_message.configure(text='Select a mouse button first!')
        return

    # validate input for initial waiting
    if not initial_delay.get().isnumeric() or int(initial_delay.get()) < 0:
        error_message.configure(text='Not valid Initial delay!')
        return
    initial_delay_time = int(initial_delay.get())

    # validate input for duration
    if not duration_element.get().isnumeric() or int(duration_element.get()) < 0:
        error_message.configure(text='Not valid Duration!')
        return
    duration = int(duration_element.get())

    error_message.configure(text='')

    time.sleep(initial_delay_time)

    if MOUSE_BTN == 'left':
        final_mouse_button = 'primary' if not swapped_primary_button() else 'secondary'
    else:
        final_mouse_button = 'primary' if swapped_primary_button() else 'secondary'


    pag.mouseDown(button=final_mouse_button)
    if duration > 0:
        time.sleep(duration)
        pag.mouseUp(button=final_mouse_button)


string_var = StringVar()

btn = Button(master=root, text='start', command=start_app)
btn.pack()

mouse_btn_label = Label(master=root, text='Select Mouse Button')
mouse_btn_label.pack()

mouse_btn = OptionMenu(root, string_var, 'left', 'right', command=update_mouse_button)
mouse_btn.pack()

initial_delay_label = Label(master=root, text='Initial delay')
initial_delay_label.pack()

initial_delay = Entry(master=root)
initial_delay.pack()

duration_label = Label(master=root, text='Duration')
duration_label.pack()

duration_element = Entry(master=root)
duration_element.pack()

error_message = Label()
error_message.pack()

def main() -> None:
    root.mainloop()

if __name__ == '__main__':
    main()