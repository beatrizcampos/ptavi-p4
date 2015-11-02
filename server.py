#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import json
import time


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        self.json2registered()
        print(diccionario)
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
                IP = self.client_address[0]
                usuario = direccion[1]
                diccionario[usuario] = IP
                expires = int(line_client[3])
                time_actual = int(time.time())
                time_actual_str = time.strftime('%Y-%m-%d %H:%M:%S',
                                                time.gmtime(time_actual))
                time_exp = int(expires + time_actual)
                time_exp_string = time.strftime('%Y-%m-%d %H:%M:%S',
                                                time.gmtime(time_exp))
                value = [IP, time_exp_string]
                diccionario[usuario] = value

                lista = []
                for Cliente in diccionario:
                    if time_actual_str >= diccionario[Cliente][1]:
                        lista.append(Cliente)

                self.wfile.write(b"SIP/2.0 200 OK" + b'\r\n\r\n')

                for usuario in lista:
                    print("Borramos del diccionario")
                    del diccionario[usuario]

                self.register2json()

    def register2json(self):
        with open('registered.json', 'w') as archivo_json:
            json.dump(diccionario, archivo_json, sort_keys=True,
                      indent=4, separators=(',', ': '))

    def json2registered(self):
        try:
            with open("registered.json", 'r') as json_fich:
                datos_json = json.load(json_fich)
            usuarios = datos_json.keys()
            for usuario in usuarios:
                diccionario[usuario] = datos[usuario]
        except:
            pass


if __name__ == "__main__":

    PORT = sys.argv[1]
    diccionario = {}
    # Creamos servidor SIPRegisterHandler y escuchamos
    serv = socketserver.UDPServer(('', int(PORT)), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    serv.serve_forever()
