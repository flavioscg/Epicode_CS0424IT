from moduli_udPork import argomenti, flooder, log, banner, scan, verbi, dictionaryAttack

def main():


    banner.banner()
    args = argomenti.argomenti()

    if args.command == 'scan':
        ip = args.ip
        port_range = args.r
        connessione = args.connessione

        print("Riassunto di ciò che hai scelto:\n")
        print(f"IP: {ip}")
        print(f"RANGE: {port_range}")
        print(f"CONNESSIONE: {connessione}\n")

        scan.scanner(ip, port_range, connessione)


    elif args.command == 'flood':
        ip = args.ip
        porta = args.porta
        threads = args.threads
        numero_pacchetti = args.numero_pacchetti
        file_di_log = args.file_di_log

        print("Riassunto di ciò che hai scelto:\n")
        print(f"IP: {ip}")
        print(f"PORTA: {porta}")
        print(f"THREADS: {threads}")
        print(f"N° PACCHETTI: {numero_pacchetti}")
        print(f"FILE LOG: {file_di_log}\n")

        flooder.attacca(ip, porta, threads, numero_pacchetti, file_di_log)
    
    elif args.command == 'verb':
        ip = args.ip
        porta = args.porta
        verbi.rivela_verbi(ip, porta)

    elif args.command == 'dictionaryAttack':
        url = args.url
        redirect = args.redirect
        dictionaryAttack.attacca(url, redirect)



if __name__ == "__main__":
    main()