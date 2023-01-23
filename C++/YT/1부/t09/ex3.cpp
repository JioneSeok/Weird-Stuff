// 알파벳을 입력 받아서 그 다음 알파벳을 출력하는 프로그램을 만들어 보시오. (z 제외)

#include <stdio.h>

int main() {
    int a;

    printf("Type an alphabet : ");
    scanf("%c", &a);

    int next = a + 1;

    printf("Your next alphabet is %c\n", next);

}