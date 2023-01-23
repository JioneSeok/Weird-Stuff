#include <stdio.h>

int main() {
    FILE *in; // 스트림, 파일을 가리키는 포인터
    int n;

    in = fopen("input.txt", "r");

    fscanf(in, "%d", &n);
    printf("%d\n", n);
}