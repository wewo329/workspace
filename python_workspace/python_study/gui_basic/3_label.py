from tkinter import *

root = Tk()
root.title("practice")

root.geometry("640x640+620+220")

label1 = Label(root, text="Hello")
label1.pack()

photo = PhotoImage(file="C:/Users/gurdn/Desktop/001.png")
label2 = Label(root, image=photo)
label2.pack()

# photo2 = PhotoImage(file="C:/Users/gurdn/Desktop/002.png")
def change():
    label1.config(text="See you again")
    global photo
    photo = PhotoImage(file="C:/Users/gurdn/Desktop/002.png")
    label2.config(image=photo)

btn = Button(root, text="Click", command=change)
btn.pack()



root.mainloop()