                #imports
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import time
                #notepad window structure
root = Tk()
root.title("Clio")
root.geometry("400x700")
root.configure(bg="#33104F")
entry = tk.Text(bg="white", fg="black", wrap="word", font=("Constantia", "12")) 
entry.place(x=10, y=90, width=380, height=600) 
entry.focus()
                #notepad def
def s():
    x = entry.get("1.0", "end-1c")
    with open("Notes.txt", "w") as file:
        file.write(x + "\n") 
    saved = tk.Label(root, text="Saved!", bg="white")
    saved.config(text="Saved!")
    saved.place(x=180, y=650)
def o():
    Tk().withdraw()
    filename = askopenfilename()
    with open(filename, "r") as file:
        entry.insert("1.0", file.read())
                #save button
save_button = tk.Button(root, text="Save", font=("Georgia", 12), command=s, bg="#D0FA66", fg="#f44848")
save_button.pack()
save_button.place(x=110, y=50)
                #open button
open_button = tk.Button(root, text="Open", font=("Georgia", 12), command=o, bg="#D0FA66", fg="#f44848")
open_button.pack()
open_button.place(x=230, y=50)

root.mainloop()
