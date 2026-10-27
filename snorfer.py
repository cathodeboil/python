import asyncio
from bleak import BleakScanner
import tkinter as tk
from tkinter import *

root = Tk()
root.title("booboof snorfer")
root.geometry("200x180")
root.configure(bg="#ebc7f2")


entry1out = tk.StringVar()
entry2out = tk.StringVar()
tk.Label(root, text="Shyckuww Itewwashun", bg="#ebc7f2", fg="#6f2c7d", font=("Georgia", 12)).pack()
entry = tk.Entry(root, textvariable = entry1out)
entry.pack(anchor = "n") 
tk.Label(root, text="Timeeowt Vawwuwwe", bg="#ebc7f2", fg="#6f2c7d", font=("Georgia", 12)).pack()
entry1 = tk.Entry(root, textvariable = entry2out)
entry1.pack(anchor = "center")
iterVal = 1
timeoutVal = 5

def snorf():
    iterVal = entry1out.get() if entry1out.get().isdigit() else 1
    timeoutVal = entry2out.get() if entry2out.get().isdigit() else 5

    i = 1
    while i < int(iterVal):
        async def main():
            devices = await BleakScanner.discover(timeout = int(timeoutVal))
            for d in devices: 
                print(d)
            print("""\n---------------------\n---------------------""")
        asyncio.run(main())
        i += 1
    if i == iterVal:
        print("All done ^~^")


snorfbutton = tk.Button(root, text ="snorf snorf!", font=("Lato Hairline", 12, "bold"), bg= "#DDC1E1", command=snorf)
snorfbutton.pack()
snorfbutton.place(x=40, y=120)
root.mainloop()
