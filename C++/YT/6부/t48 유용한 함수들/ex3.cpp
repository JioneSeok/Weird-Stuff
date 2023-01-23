// 난수 (random number)
// 게임 만들때 유용하다

#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main() {
    // seed 
    srand(time(NULL)); // 1970/01/01 00:00:00로부터 지난 시간을 초 단위로 나타낸다.
    // 시간에 따라 다른 난수를 출력 가능하다.
    for (int i = 1; i <= 10; i++) {
        printf("%d\n", rand() % 10 + 1);
    }
}

