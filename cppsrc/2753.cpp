#include <iostream>
using namespace std;

int main()
{
	int a, flag = 0;

	cin >> a;

	if (a % 400 == 0 || (a % 4 ==0 && a % 100 !=0)) {
		cout << 1;
	}
	else {
		cout << 0;
	}
	return 0;
}