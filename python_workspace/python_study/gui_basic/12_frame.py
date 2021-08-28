from tkinter import *
# import tkinter.ttk as ttk
# import time
# import tkinter.messagebox as msgbox

root = Tk()
root.title("GUI")
root.geometry("640x480+620+220") 

frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()
Button(frame_drink, text="환타").pack()


root.mainloop()