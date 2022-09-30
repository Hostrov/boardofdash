import socket
import cv2
import base64
host = '213.137.70.216' # localhost ip
port = 8089 # server used port

stream_dayta = cv2.VideoCapture(0)

socket_client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client_server.connect((host, port))

while True:
    try:
        frame = stream_dayta.read()
        encoded_jpg = base64.b64encode(frame)
        socket_client_server.sendall(encoded_jpg)
    except KeyboardInterrupt:
        stream_dayta.release()
        cv2.destroyAllWindows()
        break

