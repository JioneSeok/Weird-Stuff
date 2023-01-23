#include <stdio.h>

//행변환: 자료형을 다른 자료형으로 바꾸는 작업

int main() {
    int math = 90, korean = 95, english = 96;
    int sum = math + korean + english;
    double avg = (double)sum / 3; // 정수 출력 // (double)sum 일시적으로 sum이 실수 값이 됨.

    printf("%f\n", avg); // 93.66667

}

// 정수 / 정수 = 정수
// 실수 / 정수 = 실수
// 실수 / 실수 = 실수

// 정수 + 정수 = 정수
// 정수 + 실수 = 실수
// 실수 + 실수 = 실수