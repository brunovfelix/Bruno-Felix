#include <stdio.h>
#include <stdlib.h>

void funcao_sem_leak() {
    int *dados = (int *)malloc(100000 * sizeof(int));
    if (dados == NULL) return;  // verificacao de falha de alocacao

    for (int i = 0; i < 100000; i++) {
        dados[i] = i * i;
    }

    free(dados);  // CORRECAO: libera a memoria antes de retornar
}

int main() {
    for (int i = 0; i < 100000; i++) {
        funcao_sem_leak();
    }
    printf("Programa finalizado.\n");
    return 0;
}

// Compilar:
//   gcc -Wall -o ex3_corrigido ex3_corrigido.c
