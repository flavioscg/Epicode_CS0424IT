import requests


def rivela_verbi(ip, porta):

    if porta == 80:
        url = f"http://{ip}:{porta}"
    elif porta == 443:
        url = f"https://{ip}:{porta}"
    else:
        print("Controlla la porta inserita!")


    print(f"Verifico: {url}")

    try:
        risposta = requests.options(url)


        if 'Allow' in risposta.headers:
            metodi = risposta.headers['Allow']
            print(f"Ecco i metodi abilitati: {metodi}")
        else:
            print("Allow non è presente nella risposta\n")
    except requests.RequestException as e:
        print(f"Errore nella richiesta: {e}")

