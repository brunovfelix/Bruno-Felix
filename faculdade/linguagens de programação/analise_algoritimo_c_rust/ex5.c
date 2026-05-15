#include <stdio.h>

int *retorna_ponteiro() {
    int local = 42;
    return &local;  // retorna endereco de variavel local! — BUG
    // 'local' e destruida ao fim desta funcao
}

int main() {
    int *p = retorna_ponteiro();
    printf("Valor: %d\n", *p);

    // Chama outra funcao para sobrescrever a stack
    printf("Outro printf qualquer\n");
    printf("Valor novamente: %d\n", *p);

    return 0;
}

// Compilar (vai emitir warning -Wreturn-local-addr):
//   gcc -Wall -o ex5 ex5.c
//
// Saida: Segmentation fault (core dumped)
