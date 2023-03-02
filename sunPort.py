import pyfiglet
import sys
import socket
import time
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

target = input(str("Target IP:"))

#bANNER
print("_" * 50)
print("Scanning Target" + target)
print("Scanning started at:" + str(datetime.now()))
print("_" * 50)

try:
    
    #Procura por portas abertas no endereço enviado
    for PORT in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
             
        #Retorna às portas abertas
        result = s.connect_ex((target, PORT))
        if result == 0:
            print("[*] Port {} is Open".format(PORT))
            
except KeyboardInterrupt:
    print("\n[*] Keyboard Interrupt. Exiting...")
    sys.exit()
    
except socket.error:
    print("\n[*] Socket Error. Exiting...")
    sys.exit()
            
finally:    
    s.close()