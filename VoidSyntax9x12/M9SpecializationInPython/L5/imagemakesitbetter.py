from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Tkinter with Image")
root.geometry("400x400")

image = Image.open("VoidSyntax9x12/M9SpecializationInPython/L5/Ellen Ripley.jpeg")
image = image.resize((200, 200))   
image_tk = ImageTk.PhotoImage(image)

label1 = Label(master=root, image=image_tk, height=350, width=300)
label1.place(x=50, y=0)

label2 = Label(master=root, text="Image makes it better!")
label2.place(x=120, y=360)

root.mainloop()