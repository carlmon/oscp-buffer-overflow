# OSCP Buffer Overflow Notes

## Required Software

1. A 32-bit Windows OS (Windows 7 or 10 preferred). 64-bit Windows or Wine *might* work for some challenges.
2. [Immunity Debugger](https://www.immunityinc.com/products/debugger/) - for debugging the target application
3. [Python 2.7 (x86)](https://www.python.org/downloads/release/python-2718/) - required by Immunity and mona.py
4. [mona.py](https://github.com/corelan/mona) - useful to find gadgets (like JMP ESP)

## Vulnerable Applications

### Sync Breeze 10.0.28

1. Download the vulnerable version [from Exploit DB](https://www.exploit-db.com/exploits/42928)
2. Install it on a 32-bit host.
3. Run the client, click on `Options` > `Server` > `Enable Web Server on Port: 80`
4. Make sure you can browse to http://target/ and see the web interface. Disable firewall on target if needed.
5. Start Immunity Debugger *as administrator* and attach to the running `syncbrs.exe` process.
6. Use the POC script from Kali to see the initial buffer overflow. Build a working `windows/shell_reverse_tcp` exploit.

### Freefloat FTP Server 1.0

1. Download the vulnerable version [from Exploit DB](https://www.exploit-db.com/exploits/46763)
2. Extract and run the 32-bit version.
3. Make sure you can connect to ftp://target/ (or test that port 21 is open with nmap).
4. Start Immunity Debugger and attach to the running `FTPServer.exe` process.
    * You can also start `FTPServer.exe` directly from Immunity Debugger instead of running and attaching.
5. Use the POC script from Kali to see the initial buffer overflow. Build a working `windows/meterpreter/reverse_tcp` exploit.
    * Note: Use a relocating (ASLR) JMP ESP gadget. No stable gadgets exist in this challenge.