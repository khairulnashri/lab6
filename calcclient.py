import socket
import sys

sock = socket.socket()
host = '192.168.8.193'
port = 8080

try:
    sock.connect((host,port))
    print (' Socket successfully connected ! ')
except socket.error as e:
    print ( str(e) )

loop = True

while loop:
    print ('\n ********** MATHEMATICS EQUATION CALCULATOR ********** ')
    print (' 1. Logarithm ')
    print (' 2. Square Root ')
    print (' 3. Exponential ')
    print (' 4. Power ')
    print (' 0. Exit ')
    
    type = input ('\n Enter type of equation (e.g = 1) : ' )
    sock.send(type.encode())

    if type == '1':
        print ('\n ** Logarithm ')
        num = input('\n Enter Number : ')
        base = input('\n Enter base : ')
        sock.sendall(str.encode('\n'.join([str(num), str(base)])))
        result = sock.recv(1024)
        print ( ' Answer for log ' + num + ' base ' + base + ' : ' + str(result.decode()))

    elif type == '2':
        root = True
        while root:
            print ('\n ** Square Root ')
            num = input ('\n Enter Number : ')
            if float(num) <  0:
                print('\n Negative Number Cant Be Square Root')
            else:
                root = False
                sock.send(num.encode())
                result = sock.recv(1024)

        print ( ' Answer for square root of ' + num +' : ' + str(result.decode()))


    elif type == '3':
        print ('\n ** Exponential ')
        num = input ('\n Enter Number : ')
        sock.send(num.encode())
        result = sock.recv(1024)

        print ( ' Answer for exponential of ' + numb + ' : ' + str(result.decode()))

    elif type == '4':
        print ('\n ** Power ')
        num = input('\n Enter Number : ')
        power = input('\n Enter Power : ')
        sock.sendall(str.encode('\n'.join([str(num), str(power)])))
        result = sock.recv(1024)
        print ( ' Answer for ' + num + ' power of ' + power + ' : ' + str(result.decode()))

    elif type == '0':
        num = '0'
        sock.send(num.encode())
        sock.close()
        sys.exit()
    else:
        print ('\n Invalid input please try again !')

    input ( '\n Press Enter to Continue .. ')
