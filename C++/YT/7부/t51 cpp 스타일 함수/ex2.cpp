#include <iostream>

using namespace std;

int inventory[64] = {0};
int score = 0;

/*
// 함수 overload
void getItem(int itemId) {      // 매개변수 한개 / 개수별로 구별이 가능하다.
    inventory[itemId]++;
}

void getItem(int itemId, int cnt) {     // 매개변수 두개 / 이 함수를 호출하고 싶으면 매개변수를 두개 주면 된다.
    inventory[itemId] += cnt;
}

void getItem(int itemId, int cnt, int sc) {
    inventory[itemId] += cnt;
    score += sc;
}
*/

void getItem(int itemId, int cnt = 1, int sc = 0) { // cnt와 sc에 초깃값을 주어 한개의 함수로 나타낼 수 있다. 
    inventory[itemId] += cnt;
    score += sc;
}

int main() {
    getItem(6, 5);
    getItem(3, 2);
    getItem(3);
    getItem(11, 34, 7000);

    cout << score << endl;
    for (int i = 0; i < 16; i++) {
        cout << inventory[i] << ' ';
    }
    cout << endl;
}