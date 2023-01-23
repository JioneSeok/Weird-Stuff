/*
3. 다음과 같은 함수 정의에서 컴파일 오류가 나는 이유를 찾아 보세요.
*/

void drawRectangle(int l, int r, int t, int b) {

}

void drawRectangle(int x = 0, int y = 0, int w, int h) {
    // 디폴트 매개변수는 오른쪽부터 주어야 한다. 
    // 둘 다 매개변수를 4개 받는다. (어느걸 호출했는지 모른다.)
}