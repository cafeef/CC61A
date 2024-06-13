#include <stdio.h>
int main(){
    int x, y, z;
    puts("Digite três números: ");
    puts("Digite o primeiro número: ");
    scanf("%d", &x);
    puts("Digite o segundo número: ");
    scanf("%d", &y);
    puts("Digite o terceiro número: ");
    scanf("%d", &z);
    if ((x > y) && (x > z)) printf("%d é o maior número", x);
    if ((y > x) && (y > z)) printf("%d é o maior número", y);
    if ((z > x) && (z > y)) printf("%d é o maior número", z);

}