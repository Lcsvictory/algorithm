#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int a;
	char b[4];
	int total = 0;
	int j = 0;
	cin >> a >> b;
	for (int i = sizeof(b) - 2; i >= 0; i--) {
		total += (a * (b[i] - 48)) * (pow(10, j));
		j++;
		cout << a * (b[i]-48) << endl;
	}
	cout << total << endl;
	

	return 0;
}