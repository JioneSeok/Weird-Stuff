#include <stdio.h>

// 전역변수
int itemCnt = 0;
int money = 100;

int buyItem(int cost, int cnt) {
    // 아이템을 산다.
    if (money >= cost) {
    itemCnt += cnt;
    money -= cost;
    printf("아이템을 구매했습니다.\n");
    printf("    아이템 개수 : %d\n", itemCnt);
    printf("    잔액 : %d\n", money);
    return 0;
    }
    else {
        printf("잔액이 부족합니다.\n");
        return -1;
    }
}

int main() { 
    buyItem(3000, 5);

    // 중략
    buyItem(50, 3);
}