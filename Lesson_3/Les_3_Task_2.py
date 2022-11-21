# Напишіть програму, яка обчислює значення функції 𝑦 = cos(3x), де - 𝜋 <= x <= 𝜋.
import math

PI = math.pi
x = int(input("Enter your 'x' numer :"))
if -PI <= x <= PI:
    print("y =", math.cos(3 * x))
else:
    print("Incorrect 'x' number")