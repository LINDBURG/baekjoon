#include <stdio.h>

int main() {
	int i, x, y = 0;

	scanf("%d", &x);
	for (i = 1; i <= x; i++) {
		y += i;
	}
	printf("%d", y);
	return 0;
}

