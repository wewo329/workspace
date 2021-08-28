from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("연습")
root.geometry("640x480+620+220")
# root.geometry("640x480+100+300") # 가로 x 세로 + x좌표 + y좌표

values = [str(i) + "일" for i in range(1, 32)] # 1 ~ 31 까지의 숫자
combobox = ttk.Combobox(root, height=10, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0)
readonly_combobox.pack()

def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())
    
btn = Button(root, text="choose", command=btncmd)
btn.pack()

root.mainloop()