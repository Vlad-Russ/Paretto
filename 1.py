import math
import json

#
# x = 10
# a = (x ** 7 + 22 * x ** 2)
# b = (38 * x ** 5 - 26 * x ** 6) / (math.tan(x) - math.log10(x))
# c = ((x ** 6) / 85) - 2 * x ** 3 - 56
# resultat = a + math.sqrt(b) - c
# print(f"{resultat:.2e}")

json.loads{
	"number" : "A1",
	"model" : "A.2",
	"thickness" : 10,
	"weight" : 260,
	"RAM" : 4,
	"memory" : 64,
	"battery" : 3010,
	"camera" : 2

{
	"number" : "A2",
	"model" : "A.3",
	"thickness" : 10,
	"weight" : 200,
	"RAM" : 4,
	"memory" : 128,
	"battery" : 4030,
	"camera" : 3

}
{
	"number" : "A3",
	"model" : "Mi10",
	"thickness" : 8,
	"weight" : 200,
	"RAM" : 6,
	"memory" : 64,
	"battery" : 4160,
	"camera" : 2
}
{
	"number" : "A4",
	"model" : "Mi 10 lite",
	"thickness" : 10,
	"weight" : 190,
	"RAM" : 6,
	"memory" : 64,
	"battery" : 4820,
	"camera" : 3
}
{
	"number" : "A5",
	"model" : "Mi 10T lite",
	"thickness" : 9,
	"weight" : 200,
	"RAM" : 6,
	"memory" : 128,
	"battery" : 5000,
	"camera" : 2
}
{
	"number" : "A6",
	"model" : "Mi 10T",
	"thickness" : 8,
	"weight" : 200,
	"RAM" : 8,
	"memory" : 128,
	"battery" : 5000,
	"camera" : 3
}
{
	"number" : "A7",
	"model" : "Mi 10T pro",
	"thickness" : 9,
	"weight" : 260,
	"RAM" : 8,
	"memory" : 128,
	"battery" : 3400,
	"camera" : 3
}
{
	"number" : "A8",
	"model" : "Mi 8",
	"thickness" : 8,
	"weight" : 200,
	"RAM" : 6,
	"memory" : 64,
	"battery" : 3000,
	"camera" : 2
}
{
	"number" : "A9",
	"model" : "Mi Play",
	"thickness" : 9,
	"weight" : 200,
	"RAM" : 4,
	"memory" : 64,
	"battery" : 3300,
	"camera" : 2
}
{
	"number" : "A10",
	"model" : "Mi 9",
	"thickness" : 8,
	"weight" : 220,
	"RAM" : 6,
	"memory" : 64,
	"battery" : 4780,
	"camera" : 2
}
)
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
