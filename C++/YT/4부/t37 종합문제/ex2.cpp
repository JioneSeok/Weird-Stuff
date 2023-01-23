// 2. 다음 프로그램의 실행 결과는?

#include <stdio.h>

int useCnt[5] = {0};

void useItem(int);

int main() {
    useItem(4);
    useItem(2);
    useItem(1);
    useItem(4);
    useItem(0);

    for (int i = 0; i < 5; i++) {
        printf("슬롯 %d의 아이템을 %d번 썼습니다.\n", i, useCnt[i]);
    }
}

void useItem(int itemNum) {
    useCnt[itemNum]++;
}

/*
슬롯 0의 아이템을 1번 썼습니다.
슬롯 1의 아이템을 1번 썼습니다.
슬롯 2의 아이템을 1번 썼습니다.
슬롯 3의 아이템을 0번 썼습니다.
슬롯 4의 아이템을 2번 썼습니다.
*/