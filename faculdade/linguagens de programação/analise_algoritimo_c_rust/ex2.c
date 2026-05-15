#include <stdio.h>
#include <stdlib.h>

int main() {
    int *p = (int *)malloc(sizeof(int));
    *p = 10;
    printf("Valor: %d\n", *p);

    free(p);  // memoria liberada

    // Uso apos liberacao (use-after-free) — BUG!
    printf("Apos free: %d\n", *p);
    *p = 20;
    printf("Escrevendo apos free: %d\n", *p);

    return 0;
}

// Compilar normal (pode nao crashar, mas e comportamento indefinido):
//   gcc -Wall -o ex2 ex2.c
//
// Compilar com AddressSanitizer (detecta o erro):
//   gcc -Wall -g -fsanitize=address -o ex2 ex2.c
