#include <stdio.h>

int main() {
    int a = 10;

    int *ptr;
    ptr = &a;

    printf("a의 값 : %d\n", a);

    *ptr = 20; // a = 20;과 같다.

    printf("a의 값 : %d\n", a);
}