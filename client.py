from vidstream import  ScreenShareClient
import socket
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivymd import *
import pillow

global ip
def abc(ip):
        sender =ScreenShareClient(ip,9999)
        sender.start_stream()

req=input("do you want to self stream(N) or on other device(Y)?:")
req.lower()
if(req=="n"):
    hstnam = socket.gethostname()
    ip = socket.gethostbyname(hstnam)
    abc(ip)
else:
    ip=input("enter the ip address:")
    abc(ip)

while input("") != 'STOP':
    continue
