// continue

#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    // 1+2+4+5+7+8+10+11+13
/*
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        if ((i % 3) != 0){
            sum += i;
        }
    }
    printf("%d\n", sum);
*/
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        if ((i % 3) == 0){
            continue; // 건너뛴다.
        }
        sum += i;
    }
    printf("%d\n", sum);

}