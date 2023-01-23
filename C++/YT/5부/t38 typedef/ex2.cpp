#include <stdio.h>
/*
int main() {
    int point[2] = {3, 4}; // 좌표 배열 (순서쌍)

    printf("(%d, %d)\n", point[0], point[1]);
}
*/
int main() {
    typedef int Pair[2]; // 두개짜리 int형 배열
    Pair point = {3, 4}; // int point[2] = {3, 4};

    printf("(%d, %d)\n", point[0], point[1]);
}
