#include <stdio.h>

int main() {
    int arr[3] = {1, 2, 3};
    int *ptr = arr;

    for (int i = 0; i < 3; i++) {
        printf("%d ", *(ptr + i));
    }
    printf("\n");

    for (int i = 0; i < 3; i++) {
        printf("%d ", ptr[i]);
    }
    printf("\n");

    // arr[i] == *(arr + i) == *(ptr + i) == ptr[i] == *(i + ptr) == i[ptr]
    // c언어가 a[b] -> *(a + b)로 바꿔서 계산한다.
    
    for (int i = 0; i < 3; i++) {
        printf("%d ", i[ptr]);
    }
    printf("\n");

}