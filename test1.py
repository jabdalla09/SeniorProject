import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

canvas = tk.Canvas(root, height=400, width=400, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)


def UploadAction(event=None):
    filename = filedialog.askopenfilenames()
    print("Selected:", filename)


button = tk.Button(root, text='Upload PDB Files', command=UploadAction)
button2 = tk.Button(root, text='Upload MRC/MAP Files', command=UploadAction)


button.pack()
button2.pack()
root.mainloop()
