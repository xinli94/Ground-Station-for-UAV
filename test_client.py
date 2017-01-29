# -*- coding: utf-8 -*-

import sys,socket,struct,time

if __name__=='__main__':
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1',8008))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    i=5
    while i:
        i=i-1
        time.sleep(1)
        send_bytes=struct.pack("@BBBBiiiiiiiiiiiiiiiiiiiiiiiiifffffffffBBBBBBBBBBBBBBBB",\
                                0xff,0xaa,0xbb,0x0,132,0,1,2,3,4,5,6,7,8,9,\
                                0,1,2,3,4,5,6,7,8,9,0,1,2,3,411111111,511111111,611111111,711111111,811,911111111,\
                               0.0,1.1,2.2,\
                               0x66,0x66,0x66,0x66,0x66,0x66,0x66,0x66,\
                               0x46,0x46,0x46,0x46,0x56,0x56,0x66,0x66)
        print send_bytes
        t=struct.unpack("BBBBiiiiiiiiiiiiiiiiiiiiiiiiifffffffffBBBBBBBBBBBBBBBB",send_bytes)
        print t
        s.sendall(send_bytes)
        print('sended!')
##        
##################################
##    time.sleep(1)
##    send_bytes=struct.pack("@BBBBiiiiiiiiiiiiiiiiiiiiiiiiiffffff",\
##                            0xff,0xaa,0xbb,0x1,120,10,11,12,13,14,15,16,17,18,19,\
##                            10,11,12,13,14,15,16,17,18,19,10,11,12,13,14,15,16,17,18,19)
##    print send_bytes
##    t=struct.unpack("BBBBiiiiiiiiiiiiiiiiiiiiiiiiiffffff",send_bytes)
##    print t
##    s.sendall(send_bytes)
##    print('sended!')
##    
##################################
##    i=5
##    while i:
##        i=i-1
##        time.sleep(1)
##        send_bytes=struct.pack("@BBBBiiiiiiiiiiiiiiiiiiiiiiiiiffffff",\
##                                0xff,0xaa,0xbb,0x0,120,0,1,2,3,4,5,6,7,8,9,\
##                                0,1,2,3,4,5,6,7,8,9,0,1,2,3,411111111,511111111,611111111,711111111,811111111,911111111)
##        print send_bytes
##        t=struct.unpack("BBBBiiiiiiiiiiiiiiiiiiiiiiiiiffffff",send_bytes)
##        print t
##        s.sendall(send_bytes)
##        print('sended!')
##
##
