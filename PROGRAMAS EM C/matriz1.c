/* Ler uma matriz 10 x 10 de inteiros e escrever a localização (linha e a coluna) do maior
valor */

#include <stdio.h>
int main() {
    int matriz[10][10];
    int i, j, elemento = 0, MaN = 0;
    for (i = 0; i < 10; i++) {
        for (j = 0; j < 10; j++) {
            matriz[i][j] = elemento;
            printf("%d\n", matriz[i][j]);
            if (elemento%2 == 0) {
                elemento = elemento + 8;
            }
            if (elemento%3 == 0) {
                elemento = elemento + 4;
            }
            else {
                elemento = elemento - 10;
            }
            if (elemento > MaN) {
                MaN = elemento;
            }
            elemento++;
        }
    }
    printf("O maior número é: %d\n", MaN);
}