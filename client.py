#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.
try:

    (_, SERVER, PORT, METODO, LOGIN, EXPIRES) = sys.argv

except IndexError:
    sys.exit("Usage: client.py ip puerto register sip_address expires_value")

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, int(PORT)))

Mensaje_Metodo = (METODO.upper() + " sip:" + LOGIN + " SIP/2.0\r\n")
Mensaje_Expire = ("Expires: " + str(EXPIRES) + "\r\n")
print("Enviando: " + Mensaje_Metodo + Mensaje_Expire)

# Lo enviamos
my_socket.send(bytes(Mensaje_Metodo, 'utf-8')
               + bytes(Mensaje_Expire, 'utf-8') + b'\r\n')

data = my_socket.recv(1024)


print('Recibido -- ', data.decode('utf-8'))
print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")
