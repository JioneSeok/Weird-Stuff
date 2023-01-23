// reference 변수

#include <iostream>

using namespace std;
/*
int main() {
    int a(5);
    int &p = a;
    p = 10;

    cout << p << endl;
    cout << a << endl;
}
*/

int main() {
// r-value

    int a(5);
    int &r1 = a;
    int &&r2 = 3;
}