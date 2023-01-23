// call by value : 값에 의한 호출
// call by reference : 참조에 의한 호출

#include <stdio.h>

void swap(int *x, int *y) { // 포인터 사용
    int tmp = *x; 
    *x = *y;
    *y = tmp;
}

int main() {
    // 두개의 변수의 순서를 바꿈
    int a, b;

    scanf("%d%d", &a, &b);

    swap(&a, &b);

    printf("%d %d\n", a,b);
}