// #1. 출력된 결과는?

#include <stdio.h>

int main() {
    int arr[3][3] = {0};

    printf("%d\n", &arr);
    printf("%d\n", arr);
    printf("%d\n", *arr);

    printf("%d\n", &arr[0]);
    printf("%d\n", arr[0]);
    printf("%d\n", *arr[0]);

    printf("%d\n", &arr[0][0]);

    printf("%d\n", arr[0][0]);
}
/*
100
100
100

100
100
0

100
0
*/