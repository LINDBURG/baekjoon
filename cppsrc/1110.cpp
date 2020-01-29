#include <stdio.h>
#include <stdlib.h>

int main() {
	int num, cnt = 0, tmp, a, b;

	scanf("%d", &num);
	a = num / 10;
	b = num % 10;
	while (1) {
		tmp = (a + b) % 10;
		a = b;
		b = tmp;
		cnt++;
		if ((a == num / 10) && (b == num % 10)) {
			break;
		}
	}
	printf("%d", cnt);
	return 0;
}

