import math
import json


x = 10
a = (x ** 7 + 22 * x ** 2)
b = (38 * x ** 5 - 26 * x ** 6) / (math.tan(x) - math.log10(x))
c = ((x ** 6) / 85) - 2 * x ** 3 - 56
resultat = a + math.sqrt(b) - c
print(f"{resultat:.2e}")

a = [[0, 0, 60, 60, 60, 60], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
n = 0
for i in range(3):
    for j in range(6):
        print(a[i][j], a[i + 1][j], end=' / ')
        if j <= 1:
            if a[i][j] <= a[i + 1][j]:
                n = n + 1
            else:
                n == 0
        else:
            if a[i][j] >= a[i + 1][j]:
                n = n + 1
            else:
                n == 0
    if n == 6:
        print('True')
    else:
        print('Fail')

print()
