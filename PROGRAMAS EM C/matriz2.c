/* Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais
elementos. Escreva ao final a matriz obtida */
#include <stdio.h>
int main() {
    int matriz[5][5];
    int i, j;
    for (i = 0; i < 5; i++) {
        for (j = 0; j < 5; j++) {
            if (i == j) {
                matriz[i][j] = 1;
            }
            else {
                matriz[i][j] = 0;
            }
        }
        
    }
    
}