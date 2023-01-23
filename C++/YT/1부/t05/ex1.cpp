#include <stdio.h>

int main() {
    /*
    // int: 32비트(4바이트), 정수를 담는 데 쓰임
    int a = 5;
    int b = 3;
    
    int hap = a + b;
    int cha = a - b;
    int gop = a * b;
    int mok = a / b; // 5를 3으로 나눈 몫
    int namuji = a % b; //a를 b로 나눈 나머지 (5 % 2 = 1)

    printf("%d + %d = %d\n", a, b, hap);
    printf("%d - %d = %d\n", a, b, cha);
    printf("%d * %d = %d\n", a, b, gop);
    printf("%d / %d = %d\n", a, b, mok);
    printf("%d %% %d = %d\n", a, b, namuji); // %를 실행하고 싶으면 %%사용
    */
    
    // float: 32비트(4바이트), 실수를 담는 데 쓰임
    float a = 5;
    float b = 3;
    
    float hap = a + b;
    float cha = a - b;
    float gop = a * b;
    float mok = a / b; // 5를 3으로 나눈 몫

    printf("%f + %f = %f\n", a, b, hap);
    printf("%f - %f = %f\n", a, b, cha);
    printf("%f * %f = %f\n", a, b, gop);
    printf("%f / %f = %f\n", a, b, mok);

    /*
    float, double 차이점
    부동소수점 (floating point)
    double (64bit) float보다 정확도가 더 상승함
    */
}