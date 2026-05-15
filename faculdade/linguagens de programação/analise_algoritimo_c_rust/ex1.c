#include <stdio.h>

int main() {
    int vetor[5] = {1, 2, 3, 4, 5};
    int segredo = 42;

    printf("Antes segredo = %d\n", segredo);

    // Acessa posicoes alem do limite do vetor (BUG!)
    for (int i = 0; i <= 6; i++) {
        vetor[i] = 0;  // i=5 e i=6 estao fora dos limites!
    }

    printf("Depois segredo = %d\n", segredo);

    return 0;
}

// Compilar SEM protecao de stack (para ver o bug):
//   gcc -Wall -fno-stack-protector -o ex1 ex1.c
//
// Compilar COM protecao (comportamento padrao):
//   gcc -Wall -o ex1 ex1.c
