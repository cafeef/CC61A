//A partir da leitura do valor do comprimento dos dois catetos de um triângulo retângulo, calcular e mostrar o valor da hipotenusa.
#include <stdio.h>
#include <math.h>
int main(){
    int cat1;
    int cat2;
    int hipotenusa;
    puts("Digite o comprimento do cateto 1: ");
    scanf("%d", &cat1);
    puts("Digite o comprimento do cateto 2: ");
    scanf("%d", &cat2);
    hipotenusa = pow(cat1, 2) + pow(cat2, 2);
    printf("A hipotenusa é %d", hipotenusa);
    return 0;

}