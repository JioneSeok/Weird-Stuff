#include <stdio.h>

struct Point {int x, y;}; // typedef struct {int x, y;} Point; 와 같다. 주로 전역 변수로 자주 쓴다.


int main() {
    

    Point p;

    p.x = 3;
    p.y = 4;

    printf("(%d, %d)\n", p.x, p.y);
    
}
