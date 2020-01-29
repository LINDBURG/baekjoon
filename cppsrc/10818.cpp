#include <stdio.h>
#include <stdlib.h>

int main() {
	int num, a, min =1000000, max= -1000000;

	scanf("%d", &num);
	for (int i = 0; i < num; i++) {
		scanf("%d", &a);
		if (a < min) {
			min = a;
		}
		if (a > max) {
			max = a;
		}
	}
	printf("%d %d", min, max);
	return 0;
}

