#include <stdio.h>
#include <stdlib.h>

int main() {
	int num, max = 0, tmp, sum = 0;
	double avg;

	scanf("%d", &num);
	for (int i = 0; i < num; i++) {
		scanf("%d", &tmp);
		if (max < tmp) {
			max = tmp;
		}
		sum += tmp;
	}
	avg = (double)(100 * sum) / (double)(num * max);
	printf("%.6f", avg);
	return 0;
}

