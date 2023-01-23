#include <iostream>

using namespace std;

int n;
void set() {
    n = 10;
}

namespace doodle {
    int n;
    void set() {
        n = 20;
    }

    namespace google{
        int n;
        void set() {
            n = 30;
        }
    }
}

int main() {
    using namespace std;
    using namespace doodle;

    ::set();
    doodle::set(); // ::set()으로 doodle을 생략할 수 없다. 위와 구분이 불가능하기 때문
    google::set(); // doodle을 생략 할 수 있다. 

    cout << ::n << endl;
    cout << doodle::n << endl;
    cout << doodle::google::n << endl;
}