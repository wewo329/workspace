from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as msgbox
from PIL import Image
import os

root = Tk()
root.title("합치기")

# 파일추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요.", \
        filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")), \
        initialdir=r"C:\Users\gurdn\Desktop\python_Workspace\gui_project\image")

    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END, file)

def del_file():
    L_select = list_file.curselection()
    for index in reversed(L_select):
        list_file.delete(index)

# 저장 경로 함수
def browse_dest_path():
    folder_selected = filedialog.askdirectory(title="저장할 폴더를 선택하세요.")
    if folder_selected is None:
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# 이미지 통합 함수
def merge_images():
    #  print(list_file.get(0, END))
    images = [Image.open(x) for x in list_file.get(0, END)]
    widths = [x.size[0] for x in images]
    heights = [x.size[1] for x in images]

    # [(10, 10), (20, 20), (30, 30)]

    # 최대 넓이, 전체 높이
    max_width, total_height = max(widths), sum(heights)

    # 스케치북 준비
    result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255))
    y_offset = 0 # y 위치 정보
    # for img in images:
    #     result_img.paste(img, (0, y_offset))
    #     y_offset += img.size[1] # 높이값만큼 y값 플러스
    
    for idx, img in enumerate(images):
        result_img.paste(img, (0, y_offset))
        y_offset += img.size[1] # 높이값만큼 y값 플러스
    
        progress = (idx + 1) / len(images) * 100 # 현재 진행 퍼센트
        p_var.set(progress)
        progress_bar.update()

    dest_path = os.path.join(txt_dest_path.get(), "nado_photo.jpg")
    result_img.save(dest_path)
    msgbox.showinfo("알림", "작업이 완료되었습니다.")


# 시작 함수
def start():
    print("가로넓이 : ", cmb_width.get())
    print("간격 : ", cmb_space.get())
    print("포맷 : ", cmb_format.get())

    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요.")
        return
    
    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요.")
        return
    
    # 이미지 통합 작업
    merge_images()

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일 추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택 삭제", command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4, padx=5, pady=5) # 높이 변경

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
opt_frame = LabelFrame(root, text="옵션")
opt_frame.pack(padx=5, pady=5, ipady=5)

# 1. 가로 넓이 옵션 frame
width_frame = Frame(opt_frame)
width_frame.pack(side="left", padx=10, pady=5)

    # 가로 넓이 레이블
lbl_width = Label(width_frame, text="가로넓이")
lbl_width.pack(side="left")

    # 가로 넓이 콤보박스
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(width_frame, state="readonly", values=opt_width, width=7)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5)


# 2. 간격 옵션 frame
space_frame = Frame(opt_frame)
space_frame.pack(side="left", padx=10, pady=5)

    # 간격 옵션 레이블
lbl_space = Label(space_frame, text="간격")
lbl_space.pack(side="left", padx=5)

    # 간격 옵션 콤보박스
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(space_frame, state="readonly", values=opt_space, width=7)
cmb_space.current(0)
cmb_space.pack(side="left")

# 3. 파일 포맷 옵션 frame
format_frame = Frame(opt_frame)
format_frame.pack(side="left", padx=10, pady=5)

    # 파일 포맷 옵션 레이블
lbl_format = Label(format_frame, text="포맷")
lbl_format.pack(side="left", padx=5)

    # 파일 포맷 옵션 콤보박스
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(format_frame, state="readonly", values=opt_format, width=7)
cmb_format.current(0)
cmb_format.pack(side="left")

# 진행 상황 프레임
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# 시작 닫기 프레임
run_frame = Frame(root)
run_frame.pack(fill="x", padx=5, pady=5)

btn_close = Button(run_frame, text="닫기", padx=5, pady=5, width=12, command=root.quit)
btn_close.pack(side="right", padx=5)

btn_start = Button(run_frame, text="시작", padx=5, pady=5, width=12, command=start)
btn_start.pack(side="right", padx=5)


root.resizable(False, False)
root.mainloop()