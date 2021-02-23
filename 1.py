import math
import json


x = 10
a = (x ** 7 + 22 * x ** 2)
b = (38 * x ** 5 - 26 * x ** 6) / (math.tan(x) - math.log10(x))
c = ((x ** 6) / 85) - 2 * x ** 3 - 56
resultat = a + math.sqrt(b) - c
print(f"{resultat:.2e}")

a = [[10, 260, 4, 64, 3010, 2], [10, 200, 4, 128, 4030, 3], [8, 200, 6, 64, 4160, 2]]
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
