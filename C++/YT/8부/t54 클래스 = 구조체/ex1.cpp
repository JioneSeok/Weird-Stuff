// 클래스 = 자료 저장 + 자료 처리 = 변수 + 함수
// 클래스(타입): 특정한 용도를 수행하기 위한 변수와 함수를 모아둔 틀 (자료형)
// 객체(object): 그 틀을 이용하여 찍어낸 개체(변수, 메모리 상의 공간)

#include <iostream>

using namespace std;

// private, protected, public

class TV { // 기본적으로 private의 성질을 가지고 있어서 public을 써주어야 한다.
    bool powerOn;
    int channel;
    int volume;

public:
    void on() {
        powerOn = true;
        cout << "TV를 켰습니다." << endl;
    }

    void off() {
        powerOn = false;
        cout << "TV를 껐습니다." << endl;
    }

    void setChannel(int cnl) {
        if (cnl >= 1 && cnl <= 999) {
            channel = cnl;
            cout << "채널을 " << cnl << "(으)로 바꿨습니다." << endl;
        }
    }

    void setVolume(int vol) {
        if (vol >= 0 && vol <= 100) {
            volume = vol;
        cout << "볼륨을 " << vol << "(으)로 바꿨습니다." << endl;

        }
    }
};

int main() {
    TV lg;

    lg.on();
    lg.setVolume(50);
    lg.setChannel(40);

}