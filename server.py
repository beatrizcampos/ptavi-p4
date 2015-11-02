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
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            line_client = line.split(' ')
       
            if line_client[0] == 'REGISTER':
                #Guardamos dirección registrada y la IP en un diccionario
                direccion = line_client[1].split(':')
                diccionario = dicc[direccion[1]]
                print(" Enviamos SIP/2.0 200 OK")

            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":

    PORT = sys.argv[1]
    diccionario = {}
    # Creamos servidor SIPRegisterHandler y escuchamos
    serv = socketserver.UDPServer(('', int(PORT)), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    serv.serve_forever()
