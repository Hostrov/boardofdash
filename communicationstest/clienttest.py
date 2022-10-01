import socket

ip = socket.gethostname()

ketofshock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ketofshock.connect(ip, 6)
print("ahahfhahh")