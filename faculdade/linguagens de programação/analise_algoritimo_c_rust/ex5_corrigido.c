#include <stdio.h>
#include <stdlib.h>

// CORRECAO: aloca no heap — valido apos retorno da funcao
int *retorna_ponteiro() {
    int *p = (int *)malloc(sizeof(int));
    if (p == NULL) return NULL;
    *p = 42;
    return p;  // ponteiro para heap: continua valido
}

int main() {
    int *p = retorna_ponteiro();

    if (p != NULL) {
        printf("Valor: %d\n", *p);
        printf("Outro printf qualquer\n");
        printf("Valor novamente: %d\n", *p);
        free(p);   // chamador e responsavel por liberar
        p = NULL;
    }

    return 0;
}

// Compilar:
//   gcc -Wall -o ex5_corrigido ex5_corrigido.c
