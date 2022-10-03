import socket

ip = "192.168.209.133"

ketofshock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ketofshock.connect((ip, 6))
print("ahahfhahh")