#include <stdio.h>

/*
struct Time {
    int h;
    int m;
    int s;
};

int totalSec(Time t) {
    return 3600 * h + 60 * m + s;
}

int main() {
    Time t = {1, 22, 48};

    // 1시간 = 60분 = 3600초
    // 1분 = 60초
    // 1 * 3600 + 22 * 60 + 48

    printf("%d\n", totalSec(t));
}
*/


struct Time {
    int h;
    int m;
    int s;

    int totalSec() {
        return 3600 * h + 60 * m + s;
    }
};

int main() {
    Time t = {1, 22, 48};

    // 1시간 = 60분 = 3600초
    // 1분 = 60초
    // 1 * 3600 + 22 * 60 + 48

    printf("%d\n", t.totalSec());
}