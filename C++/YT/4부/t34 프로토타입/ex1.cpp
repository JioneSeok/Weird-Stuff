// prototype : ����, ����ǰ

#include <stdio.h>

// �ȱ�
void walk(int distance) {
    printf("%dcm�� �ɾ����ϴ�.\n", distance);
}

// ����
void rotate(int angle) {
    printf("%d�� ȸ���߽��ϴ�.\n", angle);
}

void drawSquare() {
    for (int i = 1; i <=4; i++) {
        walk(10);
        rotate(90);
    }
}

int main() {
    drawSquare();
}