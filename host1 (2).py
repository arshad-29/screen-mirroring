from vidstream import StreamingServer
import threading
import socket

sysnam=socket.gethostname()
ip=socket.gethostbyname(sysnam)
receiver =StreamingServer(ip,9999)
a=threading.Thread(target=receiver.start_server)
a.start()

while input("") != 'STOP':
    continue

receiver.stop_server()