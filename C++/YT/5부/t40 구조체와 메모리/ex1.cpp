#include <stdio.h>

struct ProductInfo {
    int num; // 4B
    char name[100]; // 100B
    int cost; // 4B
};
// sizeof(myProduct) == 108B

int main() {
    ProductInfo myProduct = {4797283, "���� �Ѷ��", 19900};

    printf("��ǰ ��ȣ : %d\n", myProduct.num);
    printf("��ǰ �̸� : %s\n", myProduct.name);
    printf("���� : %d��\n", myProduct.cost);
}