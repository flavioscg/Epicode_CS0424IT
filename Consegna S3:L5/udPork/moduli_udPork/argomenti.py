import argparse

def argomenti():
    parser = argparse.ArgumentParser(description='Un elementare UDP flooder.')


    parser.add_argument('-ip', type=str, required=True, help="IP dell'host vittima")
    parser.add_argument('-p', '--porta', type=int, required=True, help="Porta dell'host vittima'")
    parser.add_argument('-t', '--threads', type=int, default=1, help="Numero di threads da utilizzare")
    parser.add_argument('--numero_pacchetti', type=int, default=1000, help="Numero di pacchetti")
    parser.add_argument('--file_di_log', type=str, default="udpork.log", help="Stabilisci un file per i log")
    return parser.parse_args()