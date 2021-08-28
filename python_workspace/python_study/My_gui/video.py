import cv2
from PIL import Image, ImageTk
from tkinter import messagebox

def _video_open_get_(filename):
    
    cap = cv2.VideoCapture(filename)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

    try:
        if cap.isOpened():
            ret, frame = cap.read()
            cap.release()
            return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    except:
        messagebox.showerror(title='Video file not found', message='Please select a video file.')

if __name__ == "__main__":
    print(_video_open_get_(r"D:\이츠 미\파이썬 강의\mov"))
    