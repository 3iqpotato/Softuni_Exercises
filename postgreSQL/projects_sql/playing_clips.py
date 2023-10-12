import pathlib
import psycopg2
import cv2
import pygame

import psycopg2

con = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='kiko369963'
)

cur = con.cursor()

pygame.init()

query = 'SELECT * FROM my_videos'

cur.execute(query)
data = cur.fetchall()


closed = False
for row in data:
    file_path = row[-1]
    cap = cv2.VideoCapture(file_path)
    cv2.namedWindow("Video Player", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Video Player", 980, 680)

    while (cap.isOpened()):
        success, frame = cap.read()
        if success:
            cv2.imshow('Video Player', frame)

        quitButton = cv2.waitKey(25) & 0xFF == ord('q')
        closeButton = cv2.getWindowProperty('Video Player', cv2.WND_PROP_VISIBLE) < 1

        if quitButton or closeButton:
            closed = True
            break
    else:
        break
    if closed:
        break

    cap.release()
    cv2.destroyAllWindows()