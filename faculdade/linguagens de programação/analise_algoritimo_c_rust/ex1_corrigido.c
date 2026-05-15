#include <stdio.h>

int main() {
    int vetor[5] = {1, 2, 3, 4, 5};
    int segredo = 42;

    printf("Antes segredo = %d\n", segredo);

    // CORRECAO: limite correto e i < 5 (nao i <= 6)
    for (int i = 0; i < 5; i++) {
        vetor[i] = 0;
    }

    printf("Depois segredo = %d\n", segredo);

    return 0;
}

// Compilar:
//   gcc -Wall -o ex1_corrigido ex1_corrigido.c
