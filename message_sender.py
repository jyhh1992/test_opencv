# channel open
# ip port community rule
# socket call
# send something
# 

import socket


sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sender.sendto(str.encode('Hello Sender'),'192.168.16.24', 7778)

