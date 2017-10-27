import cv2
import numpy as np
from numpy import *
#
if __name__ == '__main__':
    cap = cv2.VideoCapture('周杰伦 - 告白气球.mp4')
    # _, frame1 = cap.read()
    # frame1 = cv2.resize(frame1, (300, 300))
    # frame_start = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame_first = None

    while cap.isOpened():
        ok, frame_next = cap.read()
        frame_next = cv2.resize(frame_next, (300, 300))
        frame_next_gray = cv2.cvtColor(frame_next, cv2.COLOR_BGR2GRAY)
        frame_gauss = cv2.GaussianBlur(frame_next_gray, (21, 21), 0)

        if frame_first is None:
            frame_first = frame_gauss

        image = cv2.absdiff(frame_first, frame_gauss)

        cv2.imshow('frame1', frame_first)
        cv2.imshow('frame_next', frame_next_gray)
        cv2.imshow('image', image)
        cv2.imshow('gauss', frame_gauss)
        cv2.waitKey(10)





