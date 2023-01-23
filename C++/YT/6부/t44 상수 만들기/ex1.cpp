// 상수 : 변하지 않는 수
// 변수 : 변할 수 있는 수
// const, 매크로, enum

#include <stdio.h>

int main() {
    const float PI = 3.14159; // 보통 상수는 대문자로 쓴다.

    float a = PI;

    printf("π = %.2f\n", PI); // π입력 : ㅎ+한자
    printf("π = %d\n", &PI);
}