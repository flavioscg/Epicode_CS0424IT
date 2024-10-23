import requests

# Script rudimentale per enumerazione verbi HTTP mediante OPTIONS e risposta Allow in header. 
# Di default su http (creato esclusivamente per esercitazioni su metasploitable 2)

def main():
    # Input dell'utente per ricevere l'URL
    url = input("Inserisci URL (http://example.com): ")
    

    # Stampa dell'URL verificato
    print(f"Verifico: {url}")

    try:
        # Invio della richiesta HTTP OPTIONS
        risposta = requests.options(url)
        # Controllo del codice di stato della risposta
        if risposta.status_code == 200:
             # Controllo se l'intestazione 'Allow' è presente nella risposta
            if 'Allow' in risposta.headers:
                metodi = risposta.headers['Allow']
                print(f"Ecco i metodi abilitati: {metodi}")
            else:
                print("Allow non è presente nella risposta\n")
        else:
            print(f"Codice di stato: {risposta.status_code}")
    except requests.RequestException as e:
         # Gestione delle eccezioni per errori nella richiesta
        print(f"Errore nella richiesta: {e}")



if __name__ == "__main__":
    main()

