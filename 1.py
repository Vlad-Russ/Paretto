import math
import json

a = [[10, 260, 4, 64, 3010, 2], [10, 200, 4, 128, 4030, 3], [8, 200, 6, 64, 4160, 2]]
b = [[10, 260, 4, 64, 3010, 2], [10, 200, 4, 128, 4030, 3], [8, 200, 6, 64, 4160, 2]]

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
