#include <iostream>
#include <string>

using namespace std;

int main() {
    string str;
    str = "Hello"; // ���ڿ� ���̸� ���������� �ʾƵ� �ȴ�. 
    cout << str << endl;

    string name;

    cout << "�̸� �Է� : ";
    cin >> name;

    string message = "�ȳ��ϼ���, " + name + " ��.";
    cout << message << endl;
}