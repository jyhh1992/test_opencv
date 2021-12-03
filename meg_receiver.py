import socket

def func_recev(ip,port):
    recevier = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # socket 통신준비

    recevier.bind((ip, port))
    # 바인딩

    while True:
        bytepair = recevier.recvfrom(1024)
        # 통신 사이즈 설정

        message = bytepair[0]
        address = bytepair[1]

        print(message, '.',address)

    return

if __name__ == '__main__':

    func_recev('192.168.16.24', 7778)
    try:
        pass
    except Exception as e:
        pass

