#include <iostream>
using namespace std;

int main()
{
	int a, b;

	cin >> a >> b;


	if (b < 45) {
		a = (a + 23) % 24;
	}
	b = (b + 15) % 60;

	cout << a << " " << b;
	return 0;
}