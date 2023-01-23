/*
    n = 4
    1
    123
    12345
    1234567

    i번째 줄에서 출력 되는 숫자의 개수 -> 2 * i - 1
*/

#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= 2 * i - 1; j++) {
            printf("%d ", j);
        }
        printf("\n");
    }
}