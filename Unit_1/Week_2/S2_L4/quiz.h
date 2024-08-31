#ifndef QUIZ_H
#define QUIZ_H

#define MAX 5


void banner_iniziale();

void menu();

void carica_domande(char domande[][100], char opzioni[][4][50], char risposte[], int *numero_domande);

void inizia(char domande[][100], char opzioni[][4][50], char risposte[], int numero_domande);

void mostra_domanda(char domande[][100], char opzioni[][4][50], int numero_domanda);

char ottieni_risposta();

#endif




