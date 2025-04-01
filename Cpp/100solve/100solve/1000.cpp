#include <iostream>
using namespace std;

int main() {
	char a[5];
	
	cin.getline(a, sizeof(a));
	
	cout << a[0]-48 + a[2]-48 << endl;
	return 0;
}