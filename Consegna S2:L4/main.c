#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "quiz.h"

int main() {

    char scelta = 'O';
    char domande[MAX][100];
    char risposte[MAX];
    char opzioni[MAX][4][50];
    int numero_domande;


    banner_iniziale();

    while (scelta == 'O') {
        
        menu();
        scanf("%c", &scelta);
        switch (scelta) {
        case 'A':
        case 'a':
            carica_domande(domande, opzioni, risposte, &numero_domande);
            inizia(domande, opzioni, risposte, numero_domande);
            scelta = 'O';
        break;

        case 'B':
        case 'b':
        scelta = 'N';
        break;
        default:
        printf("\n\nAttenzione, devi effettuare una scelta!\n\n");
        scelta = 'O';


        }
    }

    return 0;
}