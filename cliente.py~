#!/usr/bin/python
import socket
import sys

serverName = 'localhost'
serverPort = 12000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


opcao = int(raw_input(" escolha : 1-somar  2-raiz quadrada  3-sair" ))
n1 = int(raw_input(("digite um numero :")))
n2 = int(raw_input(("digite outro numero :")))

byte_msg = repr(opcao)
'''int(byte_msg1) = n1.encode('utf-8')
int(byte_msg2) = n2.encode('utf-8')'''



clientSocket.sendto(byte_msg(serverName, serverPort))
opcao,serverAddress= clientSocket.recvfrom(2048)
print(clientSocket)

print(opcao)
print(opcao.decode('utf-8'))
clientSocket.close()
