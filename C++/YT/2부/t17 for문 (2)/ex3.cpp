#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int i, sum;
    for (i = 1, sum = 0; i <= n; sum += i, i += 1);
    
    printf("%d\n", sum);
}