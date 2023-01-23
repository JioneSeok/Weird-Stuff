// this: 객체 자신을 가리키는 포인터이다.

#include <iostream>

using namespace std;
/*
class MyClass {
public:
    void PrintThis() {
        cout << "나의 주소는 " << this << endl;
    }
};

int main() {
    MyClass a, b;

    cout << "a의 주소는 " << &a << endl;
    cout << "b의 주소는 " << &b << endl;

    a.PrintThis(); // this 즉 본인의 주소값을 호출한다.
    b.PrintThis();
}
*/
class MyClass {
public:
    void PrintThis(MyClass *ptr) { // this는 매개변수가 생략된 것이다. 
        cout << "나의 주소는 " << ptr << endl;
    }
};

int main() {
    MyClass a, b;

    cout << "a의 주소는 " << &a << endl;
    cout << "b의 주소는 " << &b << endl;

    a.PrintThis(&a);
    b.PrintThis(&b);
}
// this 포인터는 MyClass 안에 있는 것이 아니라 다른 공간에 있지만 PrintThis라는 애를 통해서 어디 소속인지 알아낼 수 있다. 