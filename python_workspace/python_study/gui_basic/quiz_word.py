import os
from tkinter import *
import tkinter.messagebox as msgbox


main = Tk()
main.title("제목 없음 - Windows 메모장")
main.geometry("640x480")

# 메뉴 만들기
filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='utf8') as mynote:
            file_cont = mynote.read()
            txt_box.delete('1.0', END)
            txt_box.insert('1.0', file_cont)
    else: msgbox.showerror("error", "파일이 존재하지 않습니다.")
    
    # search = Tk()
    # search.title("파일 검색")
    # search.geometry("480x160+720+400")

    # search_box = Text(search, width=30, height=1)
    # search_box.insert(END, "찾을 파일의 이름을 입력하세요.")
    # search_box.pack()


def save_file():
    with open(filename, 'w', encoding='utf8') as mynote:
        mynote.write(txt_box.get('1.0', END))

menu = Menu(main)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=main.quit)

menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

main.config(menu=menu)

# textbox + scrollbar 만들기
scrollbar = Scrollbar(main)
scrollbar.pack(side="right", fill="y")

txt_box = Text(main, yscrollcommand=scrollbar.set)
txt_box.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt_box.yview)



main.mainloop()