from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title("Denomination Calculator")
root.geometry("600x600")
root.config(bg="lightblue")

image = Image.open("VoidSyntax9x12/M9SpecializationInPython/L6/app_image.png")
image = image.resize((300, 300))
image_tk = ImageTk.PhotoImage(image)

label_image = Label(master=root, image=image_tk, bg="lightblue")
label_image.place(x=150, y=20)

def show_message():
    message = messagebox.showinfo("Denomination Calculator", "Do you want to calculate denominations?")
    if message == "ok":
        show_top_window()

button = Button(master=root, text="Start Calculation", bg="green", fg="white", font=("Arial", 16, "bold"), command=show_message)  
button.place(x=220, y=360)  

def show_top_window():
    top = Toplevel()
    top.title("Denomination Input")
    top.geometry("600x400")
    top.config(bg="lightblue")
    
    label1_top = Label(master=top, text="Enter Total Amount:", bg="lightblue", font=("Arial", 12))
    label1_top.place(x=250, y=30)
    
    entry_amount = Entry(master=top, bg="white", fg="black", width=40)
    entry_amount.place(x=180, y=65)

    label2_top = Label(master=top, text="Here are the number of notes for each denomination:", bg="lightblue", font=("Arial", 11))
    label2_top.place(x=100, y=140)

    label_2000 = Label(master=top, text="2000", bg="lightblue", font=("Arial", 11))
    label_2000.place(x=200, y=180)
    entry_2000 = Entry(master=top, bg="white", fg="black", width=20)
    entry_2000.place(x=250, y=180)

    label_500 = Label(master=top, text="500", bg="lightblue", font=("Arial", 11))
    label_500.place(x=200, y=210)
    entry_500 = Entry(master=top, bg="white", fg="black", width=20)
    entry_500.place(x=250, y=210)

    label_100 = Label(master=top, text="100", bg="lightblue", font=("Arial", 11))
    label_100.place(x=200, y=240)
    entry_100 = Entry(master=top, bg="white", fg="black", width=20)
    entry_100.place(x=250, y=240)

    def calculate_denominations():
        global amount 
        amount = int(entry_amount.get())
        
        notes_2000 = amount // 2000
        amount %= 2000  
        notes_500 = amount // 500
        amount %= 500
        notes_100 = amount // 100

        entry_2000.delete(0, END)   
        entry_2000.insert(0, str(notes_2000))
        entry_500.delete(0, END)
        entry_500.insert(0, str(notes_500))
        entry_100.delete(0, END)
        entry_100.insert(0, str(notes_100))

    
    button_calculate = Button(master=top, text="Calculate", bg="blue", fg="white", font=("Arial", 11, "bold"), command=calculate_denominations)
    button_calculate.place(x=250, y=100)


root.mainloop()