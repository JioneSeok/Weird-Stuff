// static: 정적 <-> 동적

#include <iostream>

using namespace std;

// 0 ~ 1 float R G B

class Color {
public:
    Color() : r(0), g(0), b(0) { }
    Color(float r_, float g_, float b_) : r(r_), g(g_), b(b_) { }

    float GetR() {
        return r;
    }
        float GetG() {
        return g;
    }
        float GetB() {
        return b;
    }

    static Color MixColors(Color a, Color b) { // static(정적 method)를 사용하면 private 변수까지 사용 가능
        return Color((a.r + b.r)/2, (a.g + b.g)/2, (a.b + b.b)/2);
    }

private:
    float r;
    float g;
    float b;
};
/*
// class안에 넣는다.
Color MixColors(Color a, Color b) { 

//    Color res = Color((a.GetR() + b.GetR())/2, (a.GetG() + b.GetG())/2, (a.GetB() + b.GetB())/2);
//    return res;

   return Color((a.GetR() + b.GetR())/2, (a.GetG() + b.GetG())/2, (a.GetB() + b.GetB())/2);
}
*/

int main() {
    Color blue(0, 0, 1);
    Color red(1, 0, 0);

    Color purple = Color::MixColors(blue, red); // Color 안에 있다.

    cout << "r = " << purple.GetR() << ", g = " << purple.GetG() << ", b = " << purple.GetB() << endl;
}