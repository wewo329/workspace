from tkinter import *
import time

root = Tk()
root.title("연습")
root.geometry("640x480+620+220")
# root.geometry("640x480+100+300") # 가로 x 세로 + x좌표 + y좌표

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
listbox.insert(END, "watermelon")
listbox.insert(END, "grape")
listbox.pack()

def btncmd():
    # 삭제
    L_sel = listbox.curselection()
    for r in range(len(L_sel)):
        print(L_sel)
        listbox.delete(L_sel[0])
        L_sel = listbox.curselection()

    # 갯수 확인
    # print("리스트에는", listbox.size(), "개가 있어요")

    # 항목 확인 (시작 idx, 끝 idx)
    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    # 선택된 항목 확인 (idx값으로 반환)
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="Click me", command=btncmd)
btn.pack()

root.mainloop()