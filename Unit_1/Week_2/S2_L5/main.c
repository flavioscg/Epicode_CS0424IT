#include <stdio.h>
#include <ctype.h>
#include "funzioni.h"

int main(){

float a, b;
char scelta = '\0';

    while (scelta=='\0') {

        menu();
        scanf("%c", &scelta);

        switch(scelta){

            case 'A':
            case 'a':
            printf("Inserisci primo numero: ");
            scanf("%f", &a);
            printf("Inserisci secondo numero: ");
            scanf("%f", &b);
            printf("Il prodotto dei due numeri è: %f\n\n", moltiplica(a, b));
            break;

            case 'B':
            case 'b':
            printf("Inserisci numeratore: ");
            scanf("%f", &a);
            printf("Inserisci denominatore: ");
            scanf("%f", &b);
            printf("Risultato della divisione: %f\n\n", dividi(a, b));

            break;

            case 'C':
            case 'c':
            ins_string();
            break;

            case 'D':
            case 'd':
            scelta = 'N';
            break;

            default:
            printf("\nPer favore, effettua una una scelta corretta.\n\n\n");
            scelta = 'N';
        }

    }


    return 0;
}