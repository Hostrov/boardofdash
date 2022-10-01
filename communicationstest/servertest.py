import socket

ip = '10.0.0.38'
teksock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

teksock.bind(ip, 6)
senderip, addr = teksock.accept()

teksock.listen(10)

print(senderip, addr)