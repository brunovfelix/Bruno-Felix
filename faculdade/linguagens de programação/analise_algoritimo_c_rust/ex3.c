#include <stdio.h>
#include <stdlib.h>

void funcao_com_leak() {
    int *dados = (int *)malloc(100000 * sizeof(int));
    for (int i = 0; i < 100000; i++) {
        dados[i] = i * i;
    }
    // Esqueceu do free(dados)! — MEMORY LEAK
}

int main() {
    for (int i = 0; i < 100000; i++) {
        funcao_com_leak();
    }
    printf("Programa finalizado.\n");
    return 0;
}

// Compilar com LeakSanitizer (detecta vazamentos):
//   gcc -Wall -g -fsanitize=address -o ex3 ex3.c
//
// Cada chamada vaza: 100000 * 4 bytes = 400.000 bytes (400 KB)
