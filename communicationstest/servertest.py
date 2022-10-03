import socket

iip =  "192.168.209.133"
teksock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

teksock.bind((iip, 6))

teksock.listen(10)
ip, addr = teksock.accept()


print(ip, addr)