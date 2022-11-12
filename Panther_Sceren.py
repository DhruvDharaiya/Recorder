from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import time
print('''
Key,    Stop/Show Recording  =  Ctrl + C
''')

name = input('Enter Video Name You Want To Save: ')
print('Recording Starts In 3 Seconds...')
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
file_name = f'{name}_PantherProgramming.mp4'
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))
time.sleep(3)
print('Recording Started....')
while True:
    try:
        img = ImageGrab.grab(bbox=(0, 0, width, height))
        img_np = np.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        captured_video.write(img_final)
    except KeyboardInterrupt:
        break
try:    
    print()
    print('Recording Saved\nThanks For Using Panther_Screen')
    print('Special Thanks For " Panther Programming "')
    print('Subscribe Panther Programming Now,\n     https://www.youtube.com/channel/UC8tVyDVe7F-QUaxptI0jYaw?sub_conformation=1')
    print()
    ef = input('Press " Ctrl + C " To Show Recording. \nif You Can not Want Show Your Video, Press Enter To Exit ')
    while True:
        if ef == '':
            tp = 12
            break
        elif ef == str(ef):
            tp = ef
            tp = str(tp)
            break
        else:
            break
except KeyboardInterrupt:
    import os
    os.startfile(f'{name}_PantherProgramming.mp4')
