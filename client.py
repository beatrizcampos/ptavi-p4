#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.
try:
    #(SERVER, PORT, METODO, LOGIN, EXPIRES) = sys.argv
    SERVER = sys.argv[1]
    PORT = sys.argv[2]
    METODO = sys.argv[3]
    LOGIN = sys.argv[4]
    EXPIRES = sys.argv[5]

except IndexError, ValueError:
    sys.exit("Usage: client.py ip puerto register sip_address expires_value")

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, int(PORT)))
print("Enviando: " + "REGISTER sip:" + LOGIN + " SIP/2.0" + "\r\n")
print("Expires: " + EXPIRES + "\r\n\r\n")
my_socket.send("REGISTER sip:" + LOGIN +
               " SIP/2.0" + "Expires: " + str(EXPIRES))
data = my_socket.recv(1024)

print('Recibido -- ', data.decode('utf-8'))
print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")
