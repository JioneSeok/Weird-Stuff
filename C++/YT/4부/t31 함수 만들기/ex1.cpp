#include <stdio.h>

// ��������
int itemCnt = 0;
int money = 100;
int cost;

void buyItem() {
    // �������� ���.
    itemCnt++;
    money -= cost;
    printf("�������� �����߽��ϴ�.\n");
    printf("    ������ ���� : %d\n", itemCnt);
    printf("    �ܾ� : %d\n", money);
}

int main() { 
    cost = 30;   
    buyItem();

    // �߷�
    cost = 50;
    buyItem();
}