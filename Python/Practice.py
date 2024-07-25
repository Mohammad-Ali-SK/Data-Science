from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES


root = Tk()
root.title("Translator")
root.config(bg='Red')
root.geometry('500x700')

heading = Label(root,text='Translator',font=('Time New Roman',20))
heading.place(x=50,y=20,height=30,width=400)

frame = Frame(root).pack(side=BOTTOM)










root.mainloop()