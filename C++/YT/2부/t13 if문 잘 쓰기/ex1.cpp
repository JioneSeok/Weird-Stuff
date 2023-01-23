// 중첩 if문
// 중괄호 코딩 스타일

#include <stdio.h>

int main() {
    int a, b, c;

    scanf("%d%d%d", &a, &b, &c);

    // a > b > c
    // a > c > b
    // c > a > b

    if (a > b) {
        if (a > c) {
            printf("%d\n", a);
        }
        else { // c > a
            printf("%d\n", c);
        }
    }
    else { // b > a
        if (b > c) {
            printf("%d\n", b);
        }
        else { // c > b
            printf("%d\n", c);
        }
    }
}