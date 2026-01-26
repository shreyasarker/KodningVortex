from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Virus Detection")
root.geometry("400x400")

def detect_virus():
    messagebox.showwarning("Alert!", "Stop! Virus Detected!")

button = Button(master=root, text="Scan for Virus", bg="red", fg="white", font=("Arial", 20, "bold"),command=detect_virus)    
button.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()