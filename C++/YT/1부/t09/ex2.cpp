// 체중과 키를 입력 받아서 체질량 지수를 구하는 프로그램을 만들어 보시오.

#include <stdio.h>

int main() {
    float a, b;

    printf("What is your weight(kg) : ");
    scanf("%f", &a);
    printf("Whawt is your height(m) : ");
    scanf("%f", &b);

    float bmi = a / (b * b);

    printf("Your bmi is %f\n", bmi);

}