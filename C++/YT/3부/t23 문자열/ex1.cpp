// 문자열 : 문자들이 열거

#include <stdio.h>

int main () {
    char arr[] = "abc"; // {'a', 'b', 'c', '\0'}와 같다.

    

    printf("%d", sizeof(arr) / sizeof(char));
    
}