// 최대 최소

#include <stdio.h>

int main() {
    int n;
    int arr[100];

    printf("size of array : ");
    scanf("%d", &n);

    printf("elements : ");
    for (int i = 0; i < n; i++) {
        scanf("%d ", &arr[i]);
    }

    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (max < arr[i]) {
            max = arr[i];
        }
    }

    int min = arr[0];
    for (int i = 1; i < n; i++) {
        if (min > arr[i]) {
            min = arr[i];
        }
    }

    printf("max : %d\nmin : %d\n", max, min);
}