#include <stdio.h>
#include <stdlib.h>

int main() {
	int  a, b;

	while (1) {
		if (scanf("%d %d", &a, &b) == EOF) {
			break;
		}
		printf("%d\n", a + b);
	}
	return 0;
}

