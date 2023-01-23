#include <stdio.h>

struct ProductInfo {
    int num; // 4B
    char name[100]; // 100B
    int cost; // 4B
};
// sizeof(myProduct) == 108B

int main() {
    ProductInfo myProduct = {4797283, "제주 한라봉", 19900};

    printf("상품 번호 : %d\n", myProduct.num);
    printf("상품 이름 : %s\n", myProduct.name);
    printf("가격 : %d원\n", myProduct.cost);
}