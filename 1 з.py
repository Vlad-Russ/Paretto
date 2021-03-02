import math
import json


 x = 10
 a = (x ** 7 + 22 * x ** 2)
 b = (38 * x ** 5 - 26 * x ** 6) / (math.tan(x) - math.log10(x))
 c = ((x ** 6) / 85) - 2 * x ** 3 - 56
 resultat = a + math.sqrt(b) - c
 print(f"{resultat:.2e}")

print()
