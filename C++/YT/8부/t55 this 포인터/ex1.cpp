// this: ��ü �ڽ��� ����Ű�� �������̴�.

#include <iostream>

using namespace std;
/*
class MyClass {
public:
    void PrintThis() {
        cout << "���� �ּҴ� " << this << endl;
    }
};

int main() {
    MyClass a, b;

    cout << "a�� �ּҴ� " << &a << endl;
    cout << "b�� �ּҴ� " << &b << endl;

    a.PrintThis(); // this �� ������ �ּҰ��� ȣ���Ѵ�.
    b.PrintThis();
}
*/
class MyClass {
public:
    void PrintThis(MyClass *ptr) { // this�� �Ű������� ������ ���̴�. 
        cout << "���� �ּҴ� " << ptr << endl;
    }
};

int main() {
    MyClass a, b;

    cout << "a�� �ּҴ� " << &a << endl;
    cout << "b�� �ּҴ� " << &b << endl;

    a.PrintThis(&a);
    b.PrintThis(&b);
}
// this �����ʹ� MyClass �ȿ� �ִ� ���� �ƴ϶� �ٸ� ������ ������ PrintThis��� �ָ� ���ؼ� ��� �Ҽ����� �˾Ƴ� �� �ִ�. 