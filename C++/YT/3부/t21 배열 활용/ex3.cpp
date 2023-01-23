// 짝수의 개수

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

    int cnt = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) {
            cnt++;
        }
    }
    printf("number of even numbers : %d", cnt);
}