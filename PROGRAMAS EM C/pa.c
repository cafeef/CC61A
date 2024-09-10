#include <stdio.h>
int main() {
    int n, r, i, cont;
    printf("Digite o termo: ");
    n = scanf("%d", &n);
    printf("Digite a razão: ");
    n = scanf("%d", &r);
    printf("Digite o termo inicial: ");
    n = scanf("%d", &i);
    while (cont <= n)
    {
        i = i + r;
        printf("%d\n", i);
        cont++;
    }
}