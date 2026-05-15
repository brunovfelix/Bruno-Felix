#include <stdio.h>
#include <stdlib.h>

int main() {
    int *p = (int *)malloc(sizeof(int));
    *p = 42;
    printf("Valor: %d\n", *p);

    free(p);
    free(p);  // liberacao dupla! — BUG GRAVE

    return 0;
}

// Compilar:
//   gcc -Wall -o ex4 ex4.c
//
// Saida esperada:
//   Valor: 42
//   free(): double free detected in tcache 2
//   Aborted (core dumped)
