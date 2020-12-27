import socket

# UDP protocol
myp = socket.SOCK_DGRAM

#Network address family: IPv4
afn = socket.AF_INET

#create socket
s = socket.socket(afn,myp)

#mention ip address and port no , own ip
ip = "192.168.0.237"
port = 1234

#bind ip and port no
s.bind((ip,port))

#Recieve the signal/packet from sender
def recvmsg():
    while  True:
        x = s.recvfrom(1024)
        sender = x[1][0]
        msg = x[0].decode()
        print("\n {} : {}".format(sender,msg) )


def sendmsg():
    while True:

        msg = input("").encode()
        s.sendto(msg, ("192.168.0.104",5678))

#thread, so that multiple user can send msg parallely

import threading
from time import sleep
threading.Thread(target = recvmsg).start()
sleep(1)

threading.Thread(target = sendmsg).start()













