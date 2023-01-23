/*
1. 두 숫자를 입력 받아서 그 숫자들의 합을 출력하는 프로그램을 만들어 보시오.
*/

#include <stdio.h>

int main() {
    int a, b;

    scanf("%d%d", &a, &b);
    int sum = a + b;

    printf("%d + %d = %d\n", a, b, sum);
}
