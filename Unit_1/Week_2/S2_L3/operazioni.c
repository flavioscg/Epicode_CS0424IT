#include <stdio.h>

void menu(){
    printf("\na. Addizione");
    printf("\nb. Sottrazione");
    printf("\nc. Moltiplicazione");
    printf("\nd. Divisione");
    printf("\ne. Calcola media");
    printf("\nf. Esci dal programma\n");
    printf("\n");
    printf("Cosa vuoi fare? -> ");

}

float addizione(int n1, int n2) {
  return n1 + n2;
}

float sottrazione(int n1, int n2) {
  return n1 - n2;
}

float moltiplicazione(int n1, int n2) {
  return n1 * n2;
}

float divisione(float n1, float n2) {
  if (n2 != 0) {
    return n1 / n2;
  } else {
    printf("Errore: Non puoi dividere per zero.\n");
    return 0;
  }
}

float media(float n1, float n2) {
  return (n1 + n2) / 2;
}

