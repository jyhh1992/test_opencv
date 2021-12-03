import socket
import numpy as np
import cv2 as cv

recevier = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# socket 통신준비
recevier.bind(('192.168.16.24', 7778))
# 바인딩

# 480 * 640 * 3 / 20 = 46080
perlength = int( (480 * 640 * 3) / 20) # packet size
reallength = perlength + 1

array = list()
while True:
    message, address= recevier.recvfrom(reallength)
    # 통신 사이즈 설정

    str = message[1:46081]
    num_array = b''

    array[message[0]] =  str

    if message[0] == 19:
        for i in range(20):
            num_array += array[i]
        frame = np.fromstring(num_array, dtype=np.uint8)
        frame = frame.reshape(480,640,3)
        cv.imshow('video receiver',frame)

    pass