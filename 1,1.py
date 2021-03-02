import math
import json

a = [[10, 260, 4, 64, 3010, 2],
     [10, 200, 4, 128, 4030, 3],
     [8, 200, 6, 64, 4160, 2],
     [10, 190, 60, 64, 4820, 3],
     [9, 200, 6, 128, 5000, 2],
     [8, 200, 8, 128, 5000, 3],
     [9, 260, 128, 3400, 3],
     [8, 200, 6, 64, 3000, 2],
     [9, 200, 4, 64, 3300, 2],
     [8, 220, 6, 64, 4780, 2]]

n = 0

for i in range(1):
    for j in range(6):
        for k in range(1,2):
            print(a[i][j], a[i + k][j], end=' / ')
            if j <= 2:
                if a[i][j] < a[i + k][j]:
                    n = n + 1
                    if a[i][j] == a[i + k][j]:
                        n = n + 1
                else:
                    n = 0
                    if a[i][j] == a[i + k][j]:
                        n = n + 1
            else:
                if a[i][j] > a[i + k][j]:
                    n = n + 1
                    if a[i][j] == a[i + k][j]:
                        n = n + 1
                else:
                    n = 0
                    if a[i][j] == a[i + k][j]:
                        n = n + 1



