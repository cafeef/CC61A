#include <stdio.h>
int main() {
    float largura, altura, area;
    printf("Digite a largura do retângulo: ");
    scanf("%f", &largura);
    printf("Digite a altura do retângulo: ");
    scanf("%f", &altura);
    area = largura * altura;
    printf("A área do retângulo é: %.2f\n", area);
    return 0;
}