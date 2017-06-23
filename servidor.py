#!/usr/bin/python

import socket
import math

serverHost = 'localhost'
serverPort = 12000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((serverHost, serverPort))


print("Servidor pronto para receber: ")

opcao, clientAddress, n1, n2 = serverSocket.recvfrom(2048)

while True:

    def somar(n1,n2):
        print("chamou funcao:")
        n1 = int(raw_input(("digite um numero :")))
        n2 = int(raw_input(("digite outro numero :")))
        result = str(n1)+str(n2)
        return result

    def raiz_quadrada(n2):
        return math.sqrt(n2)

    if(opcao == "soma"):
        somar()
    elif(opcao == "raiz quadrada"):
        raiz_quadrada()
    else:
        exit()




    #print('Conexao de: ', clientAddress)
    #Processa a stringe para lestras maiusculas
    #modifiedMessage = message.upper()
    #print("\n", modifiedMessage)
    #serverSocket.sendto(modifiedMessage, clientAddress)
