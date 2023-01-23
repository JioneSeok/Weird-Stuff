#include <stdio.h>

int main() {
    //array
    int arr[] = {3, 1, 4, 1, 5, 2, 1};


    for (int i = 0; i <= sizeof(arr) / sizeof(int) - 1; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}