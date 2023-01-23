#include <iostream>

using namespace std;

// 생성자: 멤버 변수 초기화
// 소멸자: 메모리 해제

// 복소수(real, imaginary) 저장 클래스

class Complex {
public:
    Complex() {
        real = 0;
        imag = 0;
    }
    Complex(double real_, double imag_) { // overload
        real = real_;
        imag = imag_;
    }

    double GetReal() {
        return real;
    }
    void SetReal(double real_) {
        real = real_;
    }
    double GetImag() {
        return imag;
    }
    void SetImag(double imag_) {
        imag = imag_;
    }

private:
    double real;
    double imag;
};

int main() {
    Complex c1; // 아무것도 없는 complex 실행(real = 0, imag = 0)
    Complex c2 = Complex(2, 3);
    Complex c3(2, 3);
    

    cout << "c1 = " << c1.GetReal() << ", " << c1.GetImag() << endl;
    cout << "c2 = " << c2.GetReal() << ", " << c2.GetImag() << endl;
    cout << "c3 = " << c2.GetReal() << ", " << c3.GetImag() << endl;
}