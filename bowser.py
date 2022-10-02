import socket

# MADE a socket
mysock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# using the socket to connect to a URl

mysock.connect(('erp.lnmiit.ac.in',80))

cmd =" GET https://erp.lnmiit.ac.in/mis/iitmsv4eGq0RuNHb0G5WbhLmTKLmTO7YBcJ4RHuXxCNPvuIw=?enc=g4R9l5ijEYlvf3Kt0STjKQ==\r\n\r\n".encode()

mysock.send(cmd)

while True:
    data=mysock.recv(512)
    if len(data)<1:
        break
    print(data.decode())

mysock.close()
