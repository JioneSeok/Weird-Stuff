// 재귀 함수 (recursion)
// 자기 안에 자기가 존재

#include <stdio.h>

void rec(int n) { // recursion의 약자
    if (n > 5) {
        return;
    }
    printf("n = %d\n", n);
    rec(n + 1);
}

int main() {
    rec(1);
}