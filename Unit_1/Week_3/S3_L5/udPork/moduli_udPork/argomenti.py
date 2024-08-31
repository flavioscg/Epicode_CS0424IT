import argparse

def argomenti():
    parser = argparse.ArgumentParser(
                        prog='udpork',
                        description='Un elementare UDP flooder.')

    subparsers = parser.add_subparsers(dest='command', required=True)
    scan = subparsers.add_parser('scan', help='Scansione porte host')
    scan.add_argument('-ip', type=str, required=True, help="IP dell'host da scansire")
    scan.add_argument('-r', type=str, required=True, help="range di porte interessate")
    scan.add_argument('--connessione', type=str, help="Stabilire TCP o UDP")


    flood = subparsers.add_parser('flood', help='Attacco flood')
    flood.add_argument('-ip', type=str, required=True, help="IP dell'host vittima")
    flood.add_argument('-p', '--porta', type=int, required=True, help="Porta dell'host vittima")
    flood.add_argument('-t', '--threads', type=int, default=1, help="Numero di threads da utilizzare")
    flood.add_argument('--numero_pacchetti', type=int, default=1000, help="Numero di pacchetti")
    flood.add_argument('--file_di_log', type=str, default="udpork.log", help="Stabilisci un file per i log")

    verb = subparsers.add_parser('verb', help='Rilevatori di verbi')
    verb.add_argument('-ip', type=str, required=True, help="IP dell'host")
    verb.add_argument('-p', '--porta', type=int, required=True, help="Porta dell'host")

    dictionaryAttack = subparsers.add_parser('dictionaryAttack', help='Esegue un attacco dizionario')
    dictionaryAttack.add_argument('-url', type=str, required=True, help="Url del form di login")
    dictionaryAttack.add_argument('-redirect', type=str, required=True, help="Redirect in caso di login avvenuto con successo")
    return parser.parse_args()

