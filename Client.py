import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 25565
sock.bind(('', port))
found = '', ''


while found[0] != 'LD_FIND':
    msg, addr = sock.recvfrom(1024)
    found = msg.decode('utf-8').split(':')
    server_ip = addr[0]
    print(found[1])