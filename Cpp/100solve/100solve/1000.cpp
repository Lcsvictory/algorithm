#include <iostream>
using namespace std;

int main() {
	long double a, b; //long double�� 16����Ʈ�� ���(linuxȯ�濡��)

	//cout.precision(6);
	//C++���� cout ��ü�� ������ �Ӽ��߿� percision���� �⺻���� 6��.
	//���� a�� ����ϰԵǸ� ��ü �ڸ����� 6�ڸ��� ����� �Ǵ°���.
	//�ڸ����� �� ���� ����ϰ� �ʹٸ� percision�޼ҵ�� ���� �����ϸ��.

	//���⼭ fixed�� �޼ҵ峪 �ʵ尡 �ƴ� manipulator(������) ��.
	//cout��ü�� ������ �Ӽ��� �����ϴ� �Լ� ��� �����ϸ� �ɵ�.
	//fixed�� cout�� ����Ҷ� �����Ҽ������� ����ϰ� ��.
	//percision�� ��ü �ڸ����� �����ϴ°��� �ƴ϶� �Ҽ����� �ڸ����� �����ϵ��� �ٲ�.
	cin >> a >> b;
	cout.precision(9);
	cout << fixed;
	cout << a / b;

	return 0;
}