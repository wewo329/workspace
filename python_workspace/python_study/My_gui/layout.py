from tkinter import *
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
from tkinter import messagebox

# def select_path():
#     dir_path = filedialog.askopenfilename(parent=root, initialdir="/", title="Please select a directory")

class layout:
    def __init__(self, title):

        self.root = Tk()
        self.root.title(title)

        # 메뉴 생성
        menu = Menu(self.root)

        menu_file = Menu(menu, tearoff=0)
        menu_file.add_command(label="Select Video", command=self.video_open)
        menu_file.add_separator()
        menu_file.add_command(label="Exit", command=self.root.quit)

        menu.add_cascade(label="File", menu=menu_file)

        # 비디오 레이블
        self.Vid_img = PhotoImage(file=r"D:\Python_Workspace\Python_study\My_gui\image\Video_img.png")
        self.Vid_can = Canvas(self.root, width=640, height=360)
        self.Vid_can.create_image(0, 0, image=self.Vid_img, anchor = NW)
        self.Vid_can.pack(padx=30, pady=10)

        # 컨트롤 프레임
        Con_frame = Frame(self.root)
        Con_frame.pack()

        # 재생, 일시정지, 리셋 버튼 추가
        play_img = PhotoImage(file=r"D:\Python_Workspace\Python_study\My_gui\image\play.png")
        pause_img = PhotoImage(file=r"D:\Python_Workspace\Python_study\My_gui\image\pause.png")
        reset_img = PhotoImage(file=r"D:\Python_Workspace\Python_study\My_gui\image\reset.png")

        play_btn = Button(Con_frame, image=play_img, command=self.play_video)
        play_btn.pack(side="left")
        pause_btn = Button(Con_frame, image=pause_img, command=self.pause_video)
        pause_btn.pack(side="left")
        reset_btn = Button(Con_frame, image=reset_img)
        reset_btn.pack(side="left")

        # 보여주기 프레임
        show_frame = Frame(self.root)
        show_frame.pack()

        self.show_img = PhotoImage(file=r"D:\Python_Workspace\Python_study\My_gui\image\show_img.png")
        self.show_can = Canvas(show_frame, width=320, height=180)
        self.show_can.create_image(0, 0, image=self.show_img, anchor=NW)
        self.show_can.grid(row=0, column=0, rowspan=3, padx=30, pady=10)

        screen_btn = Button(show_frame, text="Screen Shot", pady=3, width=30)
        screen_btn.grid(row=0, column=1)

        # 파일 이름 설정 프레임
        name_frame = LabelFrame(show_frame, text="Please select a file name")
        name_frame.grid(row=1, column=1, ipadx=10, ipady=4, padx=30)

        self.name_entry = Entry(name_frame, width=50)
        self.name_entry.pack()

        save_btn = Button(name_frame, text="Save", pady=3, width=8)
        save_btn.pack()

        exit_btn = Button(show_frame, text="Exit", pady=3, width=30, command=self.root.quit)
        exit_btn.grid(row=2, column=1, padx=30)

        self.root.resizable(False, False)
        self.root.config(menu=menu)
        self.root.mainloop()

    def video_open(self):
        self.select_video()
        ret, frame = self.get_frame()
        if ret:
            
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
            print(self.photo.width)
            self.Vid_can.create_image(0, 0, image=self.photo, anchor=NW)

    def select_video(self):
        self.filename = filedialog.askopenfilename(title="select_video", filetypes=(("MP4 files", "*.mp4"),
                                                                                         ("WMV files", "*.wmv"), ("AVI files", "*.avi"), ("All files", "*.*")))

        self.cap = cv2.VideoCapture(self.filename)

    def get_frame(self):
        try:

            if self.cap.isOpened():
                ret, frame = self.cap.read()
                print(frame)
                print(type(frame))
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            
        except:
            
            messagebox.showerror(title='Video file not found', message='Please select a video file.')
            
    def play_video(self):
        pass

    def pause_video(self):
        pass

if __name__ == "__main__":

    layout("title")
