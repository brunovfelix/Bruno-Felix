#include <stdio.h>
#include <stdlib.h>

int main() {
    int *p = (int *)malloc(sizeof(int));
    *p = 42;
    printf("Valor: %d\n", *p);

    free(p);
    p = NULL;  // CORRECAO: anula o ponteiro apos liberar
               // Se free(p) for chamado novamente, free(NULL) nao faz nada

    // Segunda chamada agora e segura:
    free(p);   // free(NULL) e uma operacao segura
    printf("Programa encerrado sem erros.\n");

    return 0;
}

// Compilar:
//   gcc -Wall -o ex4_corrigido ex4_corrigido.c
