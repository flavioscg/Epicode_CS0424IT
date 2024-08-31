import requests
from bs4 import BeautifulSoup
import os

def ricerca_google(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(url, headers=headers)
    return response.text

def parse_risultato(html):
    soup = BeautifulSoup(html, "html.parser")
    results = []
    for g in soup.find_all('div', class_='g'):
        link = g.find('a', href=True)
        if link:
            results.append(link['href'])
    return results

def nuovo_file(base_name, extension):
    counter = 1
    new_filename = f"{base_name}.{extension}"
    while os.path.exists(new_filename):
        new_filename = f"{base_name}-{counter}.{extension}"
        counter += 1
    return new_filename

def main():
    google_dork = input("Inserisci la Google Dork: ")
    file_domini = "domini.txt"
    all_results = []

    with open(file_domini, "r") as file:
        domains = file.read().splitlines()

    for domain in domains:
        query = f"site:{domain} {google_dork}"
        html = ricerca_google(query)
        results = parse_risultato(html)
        
        if results:
            print(f"Risultati per {domain}:")
            for result in results:
                print(result)
            all_results.append((domain, results))

    export = input("Vuoi esportare i risultati in un file? (S/N): ").strip().upper()
    if export == 'S':
        filename = nuovo_file("risultati-scraper", "txt")
        with open(filename, "w") as file:
            for domain, results in all_results:
                file.write(f"Risultati per {domain}:\n")
                for result in results:
                    file.write(f"{result}\n")
                file.write("\n")
        print(f"Risultati esportati in {filename}")

if __name__ == "__main__":
    main()
