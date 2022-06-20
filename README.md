# OSCP Buffer Overflow Notes

## Required Software

1. [Immunity Debugger](https://www.immunityinc.com/products/debugger/) - for debugging the target application
2. [Python 2.7 (x86)](https://www.python.org/downloads/release/python-2718/) - required by Immunity and mona.py
3. [mona.py](https://github.com/corelan/mona) - useful to find gadgets (like JMP ESP)

## Vulnerable Applications

### Sync Breeze 10.0.28

1. Download the vulnerable version [from Exploit DB](https://www.exploit-db.com/exploits/42928)
2. Install it on a 32-bit host.
3. Run the client, click on `Options` > `Server` > `Enable Web Server on Port: 80`
4. Make sure you can browse to http://target/ and see the web interface. Disable firewall on target if needed.
5. Start Immunity Debugger **as administrator** and attach to the running `syncbrs.exe` process.
6. Use the POC script from Kali to see the initial buffer overflow and work from there to build a reverse shell exploit.

