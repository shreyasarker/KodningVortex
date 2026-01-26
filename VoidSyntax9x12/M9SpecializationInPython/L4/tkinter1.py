from tkinter import *

root = Tk()
root.title("Tkinter Window")
root.geometry("300x300")

greeting = Label(master=root,text="Hello, Programmer!", bg="cyan", fg="black")
greeting.pack()

button = Button(master=root, text="Click Me", bg="navy", fg="white")
button.pack()

entry = Entry(master=root, bg="lightyellow", fg="black", width=30)
entry.pack()

frame = Frame(master=root,relief=RAISED, borderwidth=5)
frame.pack()

label = Label(master=frame, text="Inside Frame")
label.pack()

textbox = Text(master=root, height=5, width=30, bg="lightcyan", fg="navy")
textbox.pack()

root.mainloop()