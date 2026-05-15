#include <stdio.h>
#include <stdlib.h>

int main() {
    int *p = (int *)malloc(sizeof(int));
    *p = 10;
    printf("Valor: %d\n", *p);

    free(p);
    p = NULL;  // CORRECAO: anula o ponteiro apos liberar
               // free(NULL) e seguro e nao faz nada

    // Agora qualquer uso acidental de p e detectavel:
    if (p != NULL) {
        printf("Valor: %d\n", *p);
    } else {
        printf("Ponteiro nulo, nao e possivel acessar.\n");
    }

    return 0;
}

// Compilar:
//   gcc -Wall -o ex2_corrigido ex2_corrigido.c
