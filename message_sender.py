# channel open
# ip port community rule
# socket call
# send something
# 

import socket

sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# socket 통신준비

sender.bind('192.168.16.24', 7778)
# 바인딩

sender.recvfrom(1024)
# 통신 사이즈 설정

