#include <stdio.h>
#include "operazioni.h"


int main() {

  float primo_numero,
  secondo_numero;

  char scelta = 'O';

  while (scelta == 'O') {
    menu();
    scanf("%c", &scelta);

    switch (scelta) {
    case 'A':
    case 'a':
      printf("Inserisci il primo numero: ");
      scanf("%f", &primo_numero);
      printf("Inserisci il secondo numero: ");
      scanf("%f", &secondo_numero);
      printf("\n");
      printf("Risultato: %f\n", addizione(primo_numero, secondo_numero));
      printf("\n");

      break;

    case 'B':
    case 'b':
      printf("Inserisci il primo numero: ");
      scanf("%f", &primo_numero);
      printf("Inserisci il secondo numero: ");
      scanf("%f", &secondo_numero);
      printf("\n");
      printf("Risultato: %f\n", sottrazione(primo_numero, secondo_numero));
      printf("\n");

      break;

    case 'C':
    case 'c':
      moltiplicazione(primo_numero, secondo_numero);
      printf("Inserisci il primo numero: ");
      scanf("%f", &primo_numero);
      printf("Inserisci il secondo numero: ");
      scanf("%f", &secondo_numero);
      printf("\n");
      printf("Risultato: %f\n", moltiplicazione(primo_numero, secondo_numero));
      printf("\n");

      break;

    case 'D':
    case 'd':
      divisione(primo_numero, secondo_numero);
      printf("Inserisci il primo numero: ");
      scanf("%f", &primo_numero);
      printf("Inserisci il secondo numero: ");
      scanf("%f", &secondo_numero);
      printf("\n");
      printf("Risultato: %0.3f\n", divisione(primo_numero, secondo_numero));
      printf("\n");

      break;

    case 'E':
    case 'e':
      media(primo_numero, secondo_numero);
      printf("Inserisci il primo numero: ");
      scanf("%f", &primo_numero);
      printf("Inserisci il secondo numero: ");
      scanf("%f", &secondo_numero);
      printf("\n");
      printf("Risultato: %0.1f\n", media(primo_numero, secondo_numero));
      printf("\n");

      break;

    case 'F':
    case 'f':
      scelta = 'N';
      break;
    default:
      printf("\n\nAttenzione, devi effettuare una scelta!\n\n");
      scelta = 'O';
    }
  }

  return 0;

}