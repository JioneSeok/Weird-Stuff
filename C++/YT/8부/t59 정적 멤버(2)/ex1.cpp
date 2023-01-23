// 정적 멤버 변수

#include <iostream>

using namespace std;

// int idCounter = 1; class 안으로 넣는다.

class Color {
public:
    Color() : r(0), g(0), b(0), id(idCounter++) { }
    Color(float r_, float g_, float b_) : r(r_), g(g_), b(b_), id(idCounter++) { }

    float GetR() {
        return r;
    }
        float GetG() {
        return g;
    }
        float GetB() {
        return b;
    }

    int GetId() {
        return id;
    }

    static Color MixColors(Color a, Color b) { 
        return Color((a.r + b.r)/2, (a.g + b.g)/2, (a.b + b.b)/2);
    }

    static int idCounter; 
// idCounter = 1이라고 선언 할 수 없음. 만약 idCounter가 전역 변수라면 여러 class가 있을 때, idCounter를 쓰는 class끼리의 이름 중복을 방지할 수 있다.
// 객체지향 프로그래밍에서는 전역 변수를 선언하는 것을 지양 하는것이 좋다.
private:
    float r;
    float g;
    float b;

    int id;
};

int Color::idCounter = 1;

int main() {
    Color blue(0, 0, 1);
    Color red(1, 0, 0);

    Color purple = Color::MixColors(blue, red); // Color 안에 있다.

    cout << "r = " << purple.GetR() << ", g = " << purple.GetG() << ", b = " << purple.GetB() << endl;

    cout << "r.GetId() = " << red.GetId() << endl;
    cout << "b.GetId() = " << blue.GetId() << endl;
    cout << "p.GetId() = " << purple.GetId() << endl;

}