#include <stdio.h>
#include <stdlib.h>

int main() {
	int a, b, cnt=0;
	char c[42] = { 0 };

	for (int i = 0; i < 10; i++) {
		scanf("%d", &a);
		b = a % 42;
		c[b]++;
	}
	for (int i = 0; i < 42; i++) {
		if (c[i] != 0) {
			cnt++;
		}
	}
	printf("%d", cnt);
	return 0;
}

