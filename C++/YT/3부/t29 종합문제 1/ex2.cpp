// #2. 코드를 보고 출력값 예상

#include <stdio.h>

int main() {
    int a = 10;
    int b = 20;

    int *ptr;

    ptr = &a;
    *ptr = 30;

    ptr = &b;
    *ptr = 10;

    printf("%d\n", a);
    printf("%d\n", b);
    printf("%d\n", *ptr);
}

/*
30
10
10
*/