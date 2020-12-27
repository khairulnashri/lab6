import socket
import math
import errno
import sys
from multiprocessing import Process

def ProcessStart(ssock):

     while True:
            type = ssock.recv(1024).decode()

            if type == '1':
                num, base = [float(i) for i in ssock.recv(2048).decode('utf-8').split('\n')]
                result = math.log(float(num),float(base))
                ssock.sendall(str(result).encode())

            elif type  == '2':
                num = ssock.recv(1024).decode()
                result = math.sqrt(float(num))
                ssock.sendall(str(result).encode())

            elif type  == '3':
                num = ssock.recv(1024).decode()
                result = math.exp(float(num))
                ssock.sendall(str(result).encode())

            elif type == '4':
                num, power = [float(i) for i in ssock.recv(2048).decode('utf-8').split('\n')]
                result = math.pow(num,power)
                ssock.sendall(str(result).encode())

            elif type == '0':
                sys.exit()
                break

if __name__ == '__main__':
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    port = 8080

    try:
        sock.bind((host,port))
    except socket.error as e:
        print (str(e))
        sys.exit()

    sock.listen(5)
    while True:
        try:
            ssock, addr = sock.accept()
            print ('\n Socket successfully connected !! ')
        
            p = Process(target = ProcessStart, args=(ssock,))
            p.start()

        except socket.error:
            print ('an error has occurred!')

    sock.close()
