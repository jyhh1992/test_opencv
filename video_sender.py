import socket
import cv2 as cv

cap = cv.VideoCapture(0)
sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# 480 * 640 * 3 / 20 = 46080
perlength = int( (480 * 640 * 3) / 20) # packet size
reallength = perlength + 1

while cap.isOpend():
    # isOpend debuging
    cap.read()
    ret, frame = cap.read()
    cv.resize(frame, (480,640))
    num = frame.flatten()
    # 2차원(사실 색때문에 입체 3차원)에서 1차원화
    str = num.tostring()
    #스트링으로 변경
    #480*640*3 /20 
    
    
    for i in range(20):
        sender.sendto(bytes([i]) + str[i*perlength:(i+1)*perlength],'192.168.16.24', 7778)
        pass




