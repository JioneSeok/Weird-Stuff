// over load (다중 정의)

#include <iostream>

void swap(int &a, int &b) {
    int tmp = a;
    a = b;
    b = tmp;
    
}

void swapd(double &a, double &b) {
    double tmp = a;
    a = b;
    b = tmp;
}

void swapp(int* (&a), int* (&b)) { // 레퍼런스 변수 
    int *tmp = a;
    a = b;
    b = tmp;
}

int main() {
    int a = 20, b = 30; // 자료형에 따라 함수를 바꾸어 주어야 해서 불편하다.
    double da = 2.222, db = 3.333;
    int *pa = &a, *pb = &b;

    swap(a, b);
    swapd(da, db);
    swapp(pa, pb);

    std::cout << "a : " << a << std::endl;
    std::cout << "b : " << b << std::endl;

    std::cout << "da : " << da << std::endl;
    std::cout << "db : " << db << std::endl;

    std::cout << "pa : " << *pa << std::endl;
    std::cout << "pb : " << *pb << std::endl;

}