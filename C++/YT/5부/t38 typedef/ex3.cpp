#include <stdio.h>
/*
int main() {
    char *name = "Doodle";

    printf("�̸�: %s\n", name);
}
*/

int main() {
    typedef char *String;
    String name = "Doodle"; // char *name = "Doodle";

    printf("�̸�: %s\n", name);
}