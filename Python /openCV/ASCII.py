import cv2
import os
import time

ASCII_CHARS = "@%#*+=-:. "

def frame_to_ascii(frame, width=80):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height, width_orig = frame.shape
    ratio = height / width_orig
    height = int(ratio * width * 0.55)
    frame = cv2.resize(frame, (width, height))

    ascii_frame = ""
    for row in frame:
        ascii_row = "".join(ASCII_CHARS[pixel // 25] for pixel in row)
        ascii_frame += ascii_row + "\n"
    return ascii_frame

cap = cv2.VideoCapture("/home/sumit/Downloads/videoplayback.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    ascii_img = frame_to_ascii(frame)
    os.system("clear")  # clear terminal
    print(ascii_img)
    time.sleep(1/30)  # simulate 30 FPS

cap.release()
