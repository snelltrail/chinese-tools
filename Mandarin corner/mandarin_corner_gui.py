import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

import jieba

import srt

KNOWN_WORDS = set()
SUBS = []

# Root window
root = tk.Tk()
root.title("Display a Text File")
#  root.resizable(False, False)
root.geometry("550x250")

# Text editor
text = tk.Text(root)
text.pack()
#  text.grid(column=0, row=0, sticky='nsew')


def open_subtitle():
    # file type
    filetypes = (("text files", "*.srt"), ("All files", "*.*"))
    # show the open file dialog
    f = fd.askopenfile(filetypes=filetypes, initialdir=".")

    #  lines = f.readlines()
    #  split_lines = []
    #  for line in lines:
    #  seg_list = list(jieba.cut(line, cut_all=False))
    #  split_lines += seg_list

    #  # read the text file and show its content on the Text
    #  #  text.insert('1.0', f.read())
    #  text.insert("1.0", "\n".join(split_lines))

    SUBS.append(list(srt.parse(f)))
    print(SUBS)


def read_vocab_list():
    # file type

    filetypes = (("text files", "*.txt"), ("All files", "*.*"))
    # show the open file dialog
    f = fd.askopenfile(filetypes=filetypes, initialdir=".")

    lines = f.readlines()
    lines = [i.strip() for i in lines]
    print(lines)


# open file button
open_button = ttk.Button(root, text="Choose a subtitle file", command=open_subtitle)

vocab_list_button = ttk.Button(
        root, text="Choose list of known words", command=read_vocab_list
        )

#  open_button.grid(column=0, row=1, sticky='w', padx=10, pady=10)
open_button.pack()
vocab_list_button.pack()

root.mainloop()
