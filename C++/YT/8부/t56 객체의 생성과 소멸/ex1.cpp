// ������: ��ü�� ������ �� �ڵ����� ȣ��Ǵ� �Լ�
// �Ҹ���: ��ü�� �Ҹ�� �� �ڵ����� ȣ��Ǵ� �Լ�

#include <iostream>

using namespace std;

class MyClass {
public:
    MyClass() { // ������
        cout << "�����ڰ� ȣ��Ǿ���." << endl;
    }

    ~MyClass() { // �Ҹ���
        cout << "�Ҹ��ڰ� ȣ��Ǿ���." << endl;
    }
};

// MyClass globalObj;

void testLocalObj() {
    cout << "testLocalObject �Լ� ����" << endl;
    MyClass localObj;
    cout << "testLocalObject �Լ� ��" << endl;
}

int main() {
    cout << "main �Լ� ����" << endl;
    testLocalObj();
    cout << "main �Լ� ��" << endl;
}