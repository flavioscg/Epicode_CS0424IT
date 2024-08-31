import socket

def scanner(ip, port_range, connessione):

    low_port = (int(port_range.split('-')[0]))
    high_port = (int(port_range.split('-')[1]))

    for port in range(low_port, high_port +1):
        if connessione == 'TCP': s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        else:                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        s.settimeout(1)

        try:
            if connessione == 'TCP':
                stato = s.connect_ex((ip, port))
                if stato == 0:
                    try:
                        s.send(b'HEAD / HTTP/1.0\r\n\r\n')
                        risposta = s.recv(1024).decode()
                        servizio = identifica_servizio(risposta)
                        print(f"Porta {port} aperta - servizio identificato: {servizio}")
                    except Exception as e:
                        print(f"Impossibile identificare il servizio")


                else:
                    if stato == 111:
                        print(f"{port} - CHIUSA")
                    else:
                        print(f"{port} - FILTRATA (Errore: {stato})")

            """
            #UDP PORT SCAN TEST
            else:
                s.sendto(b'', (ip, port))
                try:
                    print((s.recvfrom(1024)))
                    print(f"Porta {port} - Risposta ricevuta")
                except socket.timeout:
                    print(f"Porta {port} - Nessuna risposta")
            """

        except Exception as e:
            print(f"Porta {port} - Errore: {e}")
        finally:
            s.close()

def identifica_servizio(risposta):
    if 'SSH' in risposta:
        return "SSH"
    elif 'HTTP' in risposta or 'html' in risposta:
        return "HTTP"
    elif 'SMTP' in risposta:
        return "SMTP"
    elif 'FTP' in risposta:
        return "FTP"
    elif 'IMAP' in risposta:
        return "IMAP"
    elif 'POP3' in risposta:
        return "POP3"
    else:
        return "Non riconosco il servizio"

