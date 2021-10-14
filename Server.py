import socket
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
hn = bytes('LD_FIND' + ':' + socket.gethostname(), 'utf-8')
port = 25565
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

i = 0
while True:
    sock.sendto( hn, ('<broadcast>', port))
    time.sleep(5)
    i += 1
    print(i)
