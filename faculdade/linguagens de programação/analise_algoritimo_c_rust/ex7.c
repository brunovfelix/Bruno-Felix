#include <stdio.h>
#include <stdlib.h>

int main() {
    int *p = NULL;

    // Tentativa de desreferenciar ponteiro nulo — BUG
    printf("Valor: %d\n", *p);  // Segmentation fault!

    return 0;
}

// Compilar:
//   gcc -Wall -o ex7 ex7.c
//
// Saida: Segmentation fault (core dumped)
