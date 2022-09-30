from tkinter import *
import random

def random_update():
    labell.config(text=str(random.random()))
    root.after(1, random_update)

root = Tk()

root.title("frc dashboard")
root.geometry("1500x800")
root.configure(background='#605e5c')

labell = Label(text='1', width=100, background="lightgrey", font=('intalic', 15))
labell.pack()

stream_cameraa = Label(text="yo")
stream_cameraa.pack()


root.after(500, random_update)
root.mainloop()