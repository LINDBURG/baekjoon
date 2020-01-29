#include <stdio.h>
#include <stdlib.h>

int main() {
	int num, a,max= -1000000, idx;

	for (int i = 1; i < 10; i++) {
		scanf("%d", &a);
		if (a > max) {
			max = a;
			idx = i;
		}
	}
	printf("%d\n%d", max, idx);
	return 0;
}

