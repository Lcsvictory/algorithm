#include <iostream>
using namespace std;

int main() {
	long double a, b; //long double은 16바이트를 사용(linux환경에서)

	//cout.precision(6);
	//C++에서 cout 객체가 가지는 속성중에 percision값은 기본값이 6임.
	//따라서 a를 출력하게되면 전체 자리수가 6자리로 출력이 되는것임.
	//자릿수를 더 많이 출력하고 싶다면 percision메소드로 값을 변경하면됨.

	//여기서 fixed는 메소드나 필드가 아닌 manipulator(조작자) 임.
	//cout객체의 간단한 속성을 변경하는 함수 라고 생각하면 될듯.
	//fixed는 cout이 출력할때 고정소수점으로 출력하게 함.
	//percision이 전체 자릿수를 조절하는것이 아니라 소수점의 자릿수만 조절하도록 바꿈.
	cin >> a >> b;
	cout.precision(9);
	cout << fixed;
	cout << a / b;

	return 0;
}