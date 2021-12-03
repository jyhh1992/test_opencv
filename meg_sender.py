import socket

def func_send(ip,port):
    sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    sender.sendto(str.encode('Hello Sender'),ip,port)
    return

if __name__ == '__main__':

    func_send('192.168.16.24', 7778)
    try:
        pass
    except Exception as e:
        pass

