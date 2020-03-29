from tkinter import *
from PyDictionary import PyDictionary

root =Tk()
root.geometry('250x200')

def find_meaning():
    word=entry.get()
    dictionary = PyDictionary(word)
    Meaning = dictionary.printMeanings()
    print(Meaning)

entry = Entry(root,font=("times",15,"bold"))
entry.grid(row=2,column=2)
btn=Button(root,text="Find Meaning",command=find_meaning)
btn.grid(row=4,column=2)

root.mainloop()
