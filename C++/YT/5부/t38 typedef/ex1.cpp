// typedef (type define)
// 형을 정의 (원래 있던 형에 이름 부여) (별명)

#include <stdio.h>

int main() {
    typedef int Int32; // 자료형
    Int32 n = 20; // Int32

    printf("%d\n", n);
    printf("%d\n", sizeof(Int32));
}