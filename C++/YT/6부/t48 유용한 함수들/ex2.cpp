// sscanf / sprintf

#include <stdio.h>

int main() {
    int n;
    char str[] = "450";

    sscanf(str, "%d", &n);
    printf("%d\n", n);
}