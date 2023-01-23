// break: 반복문 한개를 빠져나옴

//숫자 입력 -> 숫자 출력
//1번쨰: 7
//2번쨰: 5
//..

#include <stdio.h>

int main() {
    for (int i = 1; ; i++) {
        int k;
        scanf("%d", &k);

    if (k ==0) {
        break;
    }
        printf("%d번째: %d\n", i, k);
    }
}



// continue
// 중첩 for문

