# channel open
# ip port community rule
# socket call
# send something
# 

import socket

recevier = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# socket 통신준비

recevier.bind('192.168.16.24', 7778)
# 바인딩

while True:
    bytepair = recevier.recvfrom(1024)
    # 통신 사이즈 설정

    message = bytepair[0]
    address = bytepair[1]

    print(message, '.',address)