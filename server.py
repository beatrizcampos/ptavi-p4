#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):

        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            line_client = line.decode('utf-8').split()
            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break
            else:
                print("Recibimos peticion")

            if line_client[0] == 'REGISTER':
                #Guardamos dirección registrada y la IP en un diccionario
                direccion = line_client[1].split(':')
                diccionario[direccion[1]] = self.client_address[0]
                print("Enviamos SIP/2.0 200 OK")
                self.wfile.write(b"SIP/2.0 200 OK")


if __name__ == "__main__":

    PORT = sys.argv[1]
    diccionario = {}
    # Creamos servidor SIPRegisterHandler y escuchamos
    serv = socketserver.UDPServer(('', int(PORT)), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    serv.serve_forever()
