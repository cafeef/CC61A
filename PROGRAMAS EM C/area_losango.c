#include <stdio.h>
int main() {
    float diagonal_maior, diagonal_menor, area;
    printf("Digite o valor da diagonal maior do losango: ");
    scanf("%f", &diagonal_maior);
    printf("Digite o valor da diagonal menor do losango: ");
    scanf("%f", &diagonal_menor);
    area = (diagonal_maior * diagonal_menor)/2;
    printf("A área do losango é %.2f", area);
}