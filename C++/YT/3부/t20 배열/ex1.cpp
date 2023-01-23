// 배열

#include <stdio.h>

int main() {

    /*
    int a1, a2, a3, a4, a5;
    a1 = 1;
    a2 = 2;
    a3 = 3;
    a4 = 4;
    a5 = 5;

    printf("%d\n", a1);
    printf("%d\n", a2);
    printf("%d\n", a3);
    printf("%d\n", a4);
    printf("%d\n", a5);
*/

    int a[5]; // 칸이 5개이다.

    for (int i = 0; i <= 4; i++) {
        a[i] = i * 5;
    }

    for (int i = 0; i <= 4; i++) {
        printf("%d\n", a[i]);
    }


    
}