// ������: + - * / % += -=
// ���ǹ�: if() switch()
// �ݺ���: while() for()

//1. ���� ���� �Է�
// 90~100 A
// 80~89 B
// 70~79 C
// 60~69 D
// 50~59 E

#include <stdio.h>

int main() {
    int grade;
    scanf("%d", &grade);

    if (grade >= 90 && grade <= 100) {
        printf("A\n");
    }
    else if (grade >= 80 && grade < 90) {
        printf("B\n");
    }
    else if (grade >= 70 && grade <80) {
        printf("C\n");
    }
    else if (grade >= 60 && grade <70) {
        printf("D\n");
    }
    else if (grade >= 50 && grade < 60) {
        printf("E\n");
    }
    else {
        printf("�߸� �Է��ϼ̽��ϴ�.\n");
    }

}