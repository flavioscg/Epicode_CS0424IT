from funzioni import perimetro
from simple_term_menu import TerminalMenu

def main():
    while True:
        print("\nScegli la figura geometrica di cui vuoi calcolare il perimetro.\n")
        options = ["Quadrato", "Cerchio", "Rettangolo", "Esci"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        selezione = options[menu_entry_index]

        if selezione == "Quadrato":
            print (f"Il perimetro del quadrato è: {perimetro.Quadrato()} ")
        elif selezione == "Cerchio":
            print(f"La circonferenza del cerchio è: {perimetro.Cerchio()}")
        elif selezione == "Rettangolo":
            print(f"Il perimetro del rettangolo è: {perimetro.Rettangolo()}")
        elif selezione == "Esci":
            perimetro.Esci()
    

if __name__ == "__main__":
    main()