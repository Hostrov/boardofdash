import socket
import cv2
import base64
host = '213.137.70.216' #server ip
port = 8089 # server used port

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(host, port)
socket.listen(10)
conn, addr = socket.accept()

while True:
    try:
        cameera = socket.recv()
        img = base64.b64decode(cameera)
        cv2.imshow('frame', img)
    except KeyboardInterrupt:
        print("keyboard was interrupte lmaos")

