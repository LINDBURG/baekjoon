#include <iostream>
using namespace std;

int main()
{
	int a, b, b0, b1, b2;

	cin >> a;
	cin >> b;

	b0 = b % 10;
	b1 = (b / 10) % 10;
	b2 = b / 100;

	cout << a * b0 << endl;
	cout << a * b1 << endl;
	cout << a * b2 << endl;
	cout << a * b;
	return 0;
}