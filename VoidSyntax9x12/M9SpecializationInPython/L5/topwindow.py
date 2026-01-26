from tkinter import *

root = Tk()
root.title("Top Window")
root.geometry("400x400")

def display_top_window():
    top = Toplevel()
    top.title("Top Level Window")
    top.geometry("200x200")
    l2 = Label(master=top, text="This is a Top Level Window")
    l2.pack()
    top.mainloop()

label = Label(master=root, text="This is Root Window")
label.pack(pady=20)
button = Button(master=root, text="Display Top Window", font=("Arial", 12, "bold"),command=display_top_window)    
button.pack(pady=20)

root.mainloop()