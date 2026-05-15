#include <stdio.h>

int main() {
    int valor = 0x41424344;  // 'A'=0x41, 'B'=0x42, 'C'=0x43, 'D'=0x44
    char *p = (char *)&valor;

    printf("Inteiro: 0x%X\n", valor);
    printf("Bytes individuais:\n");
    for (int i = 0; i < (int)sizeof(int); i++) {
        printf("  byte[%d] = 0x%02X ('%c')\n",
               i, (unsigned char)p[i], p[i]);
    }

    // Modificando byte a byte
    p[0] = 'Z';
    printf("Apos modificar byte[0]: 0x%X\n", valor);

    return 0;
}

// Compilar:
//   gcc -Wall -o ex6 ex6.c
//
// Saida esperada (little-endian x86):
//   Inteiro: 0x41424344
//   Bytes individuais:
//     byte[0] = 0x44 ('D')   <- byte menos significativo primeiro!
//     byte[1] = 0x43 ('C')
//     byte[2] = 0x42 ('B')
//     byte[3] = 0x41 ('A')
//   Apos modificar byte[0]: 0x4142435A
