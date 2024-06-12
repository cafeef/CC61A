#include <stdio.h>

#define MAX_NAME_LENGTH 50  // Define o tamanho máximo do nome

// Declaração global da variável nome_retangulo
char nome_retangulo[MAX_NAME_LENGTH];

int main() {
    float largura, altura, area;

    // Solicita ao usuário que insira o nome do retângulo
    printf("Digite o nome do retângulo: ");
    scanf("%s", nome_retangulo);  // %s para ler uma string

    // Solicita ao usuário que insira a largura do retângulo
    printf("Digite a largura do retângulo: ");
    scanf("%f", &largura);

    // Solicita ao usuário que insira a altura do retângulo
    printf("Digite a altura do retângulo: ");
    scanf("%f", &altura);

    // Calcula a área do retângulo
    area = largura * altura;

    // Exibe o nome e a área do retângulo
    printf("A área do retângulo %s é: %.2f\n", nome_retangulo, area);

    return 0;
}
