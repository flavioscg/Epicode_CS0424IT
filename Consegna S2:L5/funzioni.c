#include <stdio.h>


void menu(){

    printf("Benvenuto, sono un assistente digitale, posso aiutarti a sbrigare alcuni compiti.\n");
    printf("Come posso aiutarti?\n");
    printf("Digita:\n A, per moltiplicare due numeri.\n B, per dividere due numeri.\n C, per inserire una stringa.\n D, per uscire.\n\n");
    printf("\n-> ");
}


float moltiplica(float a, float b){
    return a * b;
}


float dividi(float a, float b){
    if (b != 0) {
        return a / b;
    } else {
        printf("Errore: Non puoi dividere per zero.\n");
        return 0;
  }
}


void ins_string(){

    char stringa[11];
	printf ("Inserisci la stringa: ");
	scanf ("%10s", stringa); 
	printf("Hai inserito: %s\n", stringa);
}

