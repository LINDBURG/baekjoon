#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int num, cnt, sum;
	char str[90];

	scanf("%d", &num);
	for (int i = 0; i < num; i++) {
		sum = 0;
		cnt = 0;
		scanf("%s", &str);
		for (int j = 0; j < strlen(str); j++) {
			if (str[j] == 'O') {
				cnt++;
				sum += cnt;
			}
			else {
				cnt = 0;
			}
		}
		printf("%d\n", sum);
	}
	return 0;
}

