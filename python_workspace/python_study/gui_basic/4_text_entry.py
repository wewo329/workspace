from tkinter import *

root = Tk()
root.title("연습")
root.geometry("640x480")
# root.geometry("640x480+100+300") # 가로 x 세로 + x좌표 + y좌표

txt = Text(root, width=30, height=5)
txt.insert(END, "글자를 입력하세요")
txt.pack()

e = Entry(root, width=30)
e.pack()
e.insert(END, "한 줄만 입력해요")

def btncmd():
    # 내용 프린트
    print(txt.get("1.0", END)) # 1 : 첫번째 라인, 0 : 0번째 column 위치
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="Click me", command=btncmd)
btn.pack()

root.mainloop()