// 구조체 포인터


#include <stdio.h>

struct ProductInfo {
    int num; 
    char name[100]; 
    int cost; 
};

int main() {
    ProductInfo myProduct = {4797283, "제주 한라봉", 19900};

    ProductInfo *ptr_product = &myProduct;

    printf("상품 번호 : %d\n", (*ptr_product).num);
    printf("상품 이름 : %s\n", (*ptr_product).name);
    printf("가격 : %d원\n", (*ptr_product).cost);

    printf("상품 번호 : %d\n", ptr_product->num);
    printf("상품 이름 : %s\n", ptr_product->name);
    printf("가격 : %d원\n", ptr_product->cost);
}