import tkinter as tk
import os

from tkinter import filedialog as fd


def file_select():
    filename = fd.askopenfilename(initialdir='/',
                                  title='Выберите файл',
                                  filetypes=(('Текстовый файл', '.txt'),
                                             ('Все файлы', '*')))
    file_path['text'] = filename
    os.startfile(filename)


window = tk.Tk()

WINDOW_WIDTH = 350
WINDOW_HEIGHT = 50

window.title('Проводник')
window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
window.config(bg='white')
window.resizable(False,
                 False)

text = tk.Label(window,
                text='Файл:',
                height=1,
                width=10,
                background='silver')
text.grid(column=1,
          row=1)

file_path = tk.Label(window,
                     text='',
                     height=1,
                     width=38,
                     background='silver')
file_path.grid(column=2,
               row=1)

button_select = tk.Button(window,
                          width=37,
                          height=1,
                          text="Выбрать файл",
                          command=file_select)
button_select.grid(column=2,
                   row=2)

window.mainloop()
