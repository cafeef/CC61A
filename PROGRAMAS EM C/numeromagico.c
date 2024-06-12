#include <stdio.h>
#include <stdlib.h>
int main(){
    int magico;
    int chute;
    magico = rand() %21;
    puts("Adivinhe o número: ");
    scanf("%d", &chute);
    if (chute == magico) puts("Número correto!");
    else {
        puts("Errado...");
        if (chute > magico) puts("Muito alto!");
        else puts("Muito baixo!");
    }
    return 0;
}