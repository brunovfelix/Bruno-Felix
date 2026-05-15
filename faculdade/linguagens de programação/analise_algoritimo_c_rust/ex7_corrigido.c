#include <stdio.h>
#include <stdlib.h>

int main() {
    int *p = NULL;

    // CORRECAO: verifica se o ponteiro e NULL antes de usar
    if (p != NULL) {
        printf("Valor: %d\n", *p);
    } else {
        printf("Erro: ponteiro nulo, nao e possivel acessar o valor.\n");
    }

    return 0;
}

// Compilar:
//   gcc -Wall -o ex7_corrigido ex7_corrigido.c
