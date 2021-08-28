from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
root.title("연습")
root.geometry("640x480+620+220")
# root.geometry("640x480+100+300") # 가로 x 세로 + x좌표 + y좌표

# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) # 10 ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop()

# btn = Button(root, text="choose", command=btncmd)
# btn.pack()

P_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=P_var2)
progressbar2.pack()

def btncmd2():
    for i in range(101):
        time.sleep(0.01) # 0.01초 대기

        P_var2.set(i) # progress bar 의 값 설정
        progressbar2.update() # ui 업데이트
        print(P_var2.get())

btn = Button(root, text="start", command=btncmd2)
btn.pack()

root.mainloop()