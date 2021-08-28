from tkinter import *
# import tkinter.ttk as ttk
# import time
import tkinter.messagebox as msgbox

root = Tk()
root.title("GUI")
root.geometry("640x480+620+220")

# 기차 예매 시스템
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

def warn():
    msgbox.showwarning("경고", "해당 좌석은 예매 완료 되었습니다.")

def err():
    msgbox.showerror("에러", "결제오류가 발생했습니다")

def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")

def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다 예매하시겠습니까?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내용이 저장되지 않았습니다. \n저장 후 끝내시겠습니까?")
    # 네 : 저장 후 종료 (True)
    # 아니오 : 저장 하지 않고 종료 (False)
    # 취소 : 프로그램 종료 취소 (None)
    print(response)

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=err, text="에러").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=yesno, text="예, 아니오").pack()
Button(root, command=yesnocancel, text="예, 아니오, 취소").pack()

root.mainloop()