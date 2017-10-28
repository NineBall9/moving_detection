import cv2
import numpy as np
from numpy import *
import argparse
import time
import datetime

#
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())


if __name__ == '__main__':
    cap = cv2.VideoCapture('We.mp4')
    # _, frame1 = cap.read()
    # frame1 = cv2.resize(frame1, (300, 300))
    # frame_start = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame_first = None

    while cap.isOpened():
        ok, frame_next = cap.read()
        text = "unoccupied"
        if not ok:
            break
        frame_next = cv2.resize(frame_next, (300, 300))
        frame_next_gray = cv2.cvtColor(frame_next, cv2.COLOR_BGR2GRAY)
        frame_gauss = cv2.GaussianBlur(frame_next_gray, (21, 21), 0)

        if frame_first is None:
            frame_first = frame_gauss

        image_delta = cv2.absdiff(frame_first, frame_gauss)
        thresh = cv2.threshold(image_delta, 25, 255, cv2.THRESH_BINARY)[1]

        thresh = cv2.dilate(thresh, None, iterations=2)
        d, cnts, asd = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for c in cnts:
            if cv2.contourArea(c) < args["min_area"]:
                continue

            (x, y, w, h) = cv2.boundingRect(c)
            print("坐标为：%d, %d, %d, %d" % (x, y, w, h))
            cv2.rectangle(frame_next, (x, y), (x+w, y+h), (255, 0, 0), 2)
            text = "occupied"

        cv2.imshow('frame1', frame_first)
        cv2.imshow('frame_next', frame_next)
        cv2.imshow('thresh', thresh)
        cv2.imshow('image_delta', image_delta)
        key = cv2.waitKey(100)
        #       &amp; 0xFF
        # if key == ord('q'):
        #     break







