// 포인터(pointer): 변수의 주소를 저장하는 변수

#include <stdio.h>

int main() {
    int a = 20; // 만약 a가 string일 경우 char 사용.

    int *ptr_a;

    ptr_a = &a;

    printf("a의 값 : %d\n", a);
    printf("a의 주솟값 : %d\n", &a);
    printf("ptr_a에 저장된 값 : %d\n", ptr_a);
    printf("ptr_a가 가리키는 변수의 값 : %d\n", *ptr_a);

}