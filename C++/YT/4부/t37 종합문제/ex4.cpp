/* 4.
* 문자열을 매개변수로 받아 그 문자열에서 공백을
*제거하여 출력하는 함수를 작성해보세요.
*/

#include <stdio.h>

void print_noSpace(char str[]) { // *str = str[]
    //작성
    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] != ' ') {
        printf("%c", str[i]);
        }
    }
}

int main() {
    print_noSpace("Hello, World!\n");
    print_noSpace("My name is Doodle\n");
}