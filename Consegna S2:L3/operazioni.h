/* 
Funzioni per lo svolgimento di alcune operazioni 
richieste per l'esercitazione in C dell'unità 1, nello specifico S2/L3
*/

#ifndef OPERAZIONI_H
#define OPERAZIONI_H

#include <stdio.h>

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

#endif