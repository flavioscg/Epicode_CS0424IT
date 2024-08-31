import math

    
def Quadrato():
    lato = float(input("Inserisci la lunghezza del lato: "))
    perimetro = lato * 4
    return perimetro

def Cerchio():
    raggio = float(input("Inserisci il valore del raggio: "))
    circonferenza = 2*math.pi*raggio
    return circonferenza

def Rettangolo():
    base = float(input("Inserisci il valore della base: "))
    altezza = float(input("Inserisci il valore dell'altezza: "))
    perimetro = (base*2)+(altezza*2)
    return perimetro

def Esci():
    quit()