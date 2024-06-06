#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "quiz.h"

#define MAX 5

void banner_iniziale(){
    printf("\n\n---\n");
    printf("Sarai in grado di rispondere ad alcune domande?\n");
    printf("Hai quattro risposte a disposizione, scegli quella corretta!\n");
    printf("---\n");
}


void menu(){
    printf("\na. Nuova partita");
    printf("\nb. Esci dal gioco\n");
    printf("\n\nCosa vuoi fare? -> ");
}


void carica_domande(char domande[][100], char opzioni[][4][50], char risposte[], int *numero_domande) {

    *numero_domande = MAX;

    strcpy(domande[0], "I ghepardi sono originari di quali due continenti?");
    strcpy(opzioni[0][0], "A) Africa e Asia");
    strcpy(opzioni[0][1], "B) Africa e America");
    strcpy(opzioni[0][2], "C) Asia e America");
    strcpy(opzioni[0][3], "D) Europa e Asia");
    risposte[0] = 'A';

    strcpy(domande[1], "Quanti giorni ci sono in una settimana?");
    strcpy(opzioni[1][0], "A) 5");
    strcpy(opzioni[1][1], "B) 6");
    strcpy(opzioni[1][2], "C) 7");
    strcpy(opzioni[1][3], "D) 8");
    risposte[1] = 'C';

    strcpy(domande[2], "Che tipo di informazioni trasporta una molecola di DNA?");
    strcpy(opzioni[2][0], "A) Genetiche");
    strcpy(opzioni[2][1], "B) Energetiche");
    strcpy(opzioni[2][2], "C) Metaboliche");
    strcpy(opzioni[2][3], "D) Strutturali");
    risposte[2] = 'A';

    strcpy(domande[3], "Chi ha scritto 'Divina Commedia'?");
    strcpy(opzioni[3][0], "A) Petrarca");
    strcpy(opzioni[3][1], "B) Boccaccio");
    strcpy(opzioni[3][2], "C) Dante");
    strcpy(opzioni[3][3], "D) Manzoni");
    risposte[3] = 'C';

    strcpy(domande[4], "Quale parte del ghepardo non ha macchie?");
    strcpy(opzioni[4][0], "A) La testa");
    strcpy(opzioni[4][1], "B) Le zampe");
    strcpy(opzioni[4][2], "C) La coda");
    strcpy(opzioni[4][3], "D) La pancia");
    risposte[4] = 'D';    
    }


    void inizia(char domande[][100], char opzioni[][4][50], char risposte[], int numero_domande) {
    int punteggio = 0;
    for (int i = 0; i < numero_domande; i++) {
        mostra_domanda(domande, opzioni, i);
        char risposta_utente = ottieni_risposta();
        if (risposta_utente == risposte[i]) { 
            printf("Bravo, risposta corretta!\n\n");
            punteggio++;
        } else {
            printf("Ops... Sbagliato! Risposta giusta: %c\n\n", risposte[i]);
        }
    }
     printf("\nPunteggio: %d/%d\n", punteggio, numero_domande);
    }

void mostra_domanda(char domande[][100], char opzioni[][4][50], int numero_domanda) {
    printf("Domanda %d: %s\n", numero_domanda + 1, domande[numero_domanda]);
    for (int i = 0; i < 4; i++) {
        printf("%s\n", opzioni[numero_domanda][i]);
    }
}


char ottieni_risposta() {
    char risposta;
    printf("\n");
    printf("Inserisci risposta: ");
    scanf(" %c", &risposta);
    printf("\n\n");
    return risposta;
}
