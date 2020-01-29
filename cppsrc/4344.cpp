#include <stdio.h>
#include <stdlib.h>

int main() {
	int num, people, cnt, sum;
	int str[1000];
	double avg;

	scanf("%d", &num);
	for (int i = 0; i < num; i++) {
		sum = 0;
		cnt = 0;
		scanf("%d", &people);
		for (int j = 0; j < people; j++) {
			scanf("%d", &str[j]);
			sum += str[j];
		}
		avg = (double)sum / (double)people;
		for (int j = 0; j < people; j++) {
			if (str[j] > avg) {
				cnt++;
			}
		}
		printf("%.3f%%\n", (double)cnt * 100 / (double)people);
	}
	return 0;
}

