from tkinter import Tk

import cv2
from tkinter import *
from PIL import ImageTk, Image


def tkintertest():
    root = Tk()
    # Create a frame
    app = Frame(root, bg="white")
    app.grid()
    # Create a label in the frame
    lmain = Label(app)
    lmain.grid()

    # Capture from camera
    cap = cv2.VideoCapture(0)

    # function for video streaming
    def video_stream():
        _, frame = cap.read()
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(1, video_stream)

    video_stream()
    root.mainloop()

tkintertest()

def write_on_image(frame, cam_num, text):
    # text
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.8 #1.3
    color = (255, 131, 0)
    thickness = 2

    var1 = 330
    var2 = 40

    if cam_num == 0: org = (20, var1)
    elif cam_num == 1: org = (200, var1)
    elif cam_num == 2: org = (375, var1)
    elif cam_num == 3: org = (560, var1)
    elif cam_num == 4: org = (745, var1)
    elif cam_num == 5: org = (930, var1)
    elif cam_num == 6: org = (1100, var1)

    elif cam_num == 7: org = (10, var2)
    elif cam_num == 8: org = (260, var2)
    elif cam_num == 9: org = (525, var2)
    elif cam_num == 10: org = (775, var2)
    elif cam_num == 11: org = (1040, var2)

    elif cam_num == -1: org = (10, 700)
    else: org = (10, 20)

    frame = cv2.putText(frame, str(text), org, font,
                        fontScale, color, thickness, cv2.LINE_AA)
    return frame
