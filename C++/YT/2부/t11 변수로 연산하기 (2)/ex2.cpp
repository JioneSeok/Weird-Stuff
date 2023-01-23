// 논리 연산자 (그리고, 또는, ...)
// && ||(shift + \) !

#include <stdio.h>

int main() {
    int a;
    scanf("%d", &a);

    bool p = (a >= 1) && (a <=10); // and
    bool q = (a == 3) || (a == 7); // or
    bool r = !q; // r은 q의 반대

    printf("%d\n", p);
    printf("%d\n", q);
    printf("%d\n", r);
}