#include <stdio.h>
#include <stdlib.h>

int main() {
	int a, b, c, mul, chk;
	char str[10] = { 0 };

	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);
	mul = a * b * c;

	while (1) {
		chk = mul % 10;
		str[chk]++;
		mul /= 10;
		if (mul == 0) {
			break;
		}
	}
	for (int i = 0; i < 10; i++) {
		printf("%d\n", str[i]);
	}
	return 0;
}

