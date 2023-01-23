// 범위 기반 for문

#include <iostream>

using namespace std;

int main() {
    int arr[10] = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3};

    for (int &n : arr) { // int n이 아닌 &n인 주소값을 주어야 n값이 바뀐다.
        cout << n << " ";
        n++;
    }
    cout << endl;

    for (int n : arr) {
        cout << n << " ";
    }
    cout << endl;
}