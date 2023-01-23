#include <iostream>
#include <string>

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
}
namespace google {
    int n;
    void set();
}

int main() {
    ::set();
    doodle::set();
    google::set();
    
    cout << ::n << endl;
    cout << doodle::n << endl;
    cout << google::n << endl;
}

void google::set() {
    n = 30;
}