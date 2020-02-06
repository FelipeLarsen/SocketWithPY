#!/usr/bin/python 

import socket

ip = raw_input("Digite o IP: ")
port = input("Digite a porta: ")

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if mysocket.connect_ex((ip, port)):
    print "- status [FECHADA]"
else:
    print "- status [ABERTA]"
