// 일의 자릿수가 3 6 9인 경우 *
// 1 2 * 4 5 * 6 7 8 *

#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        int j = (i % 10);
        if (j == 3 || j == 6 || j == 9) {
            printf("* ");
        }
        else {
            printf("%d ", i);
        }
    }
}