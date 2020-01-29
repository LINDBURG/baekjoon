#include <stdio.h>
#include <stdlib.h>

int main() {
	int  A[10000], x, num;

	scanf("%d %d", &num, &x);
	for (int i = 0; i < num; i++) {
		scanf("%d", &A[i]);
	}
	for (int i = 0; i < num; i++) {
		if (A[i] < x) {
			printf("%d ", A[i]);
		}
	}
	return 0;
}

