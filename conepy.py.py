import sys
sys.stdout.reconfigure(encoding='utf-8')

from decimal import Decimal, getcontext, ROUND_DOWN, ROUND_HALF_UP

# High precision for pi calculations
getcontext().prec = 100  # changed from 220 to 100

# High-precision pi
pi = Decimal(
    "3.14159265358979323846264338327950288419716939937510"
    "58209749445923078164062862089986280348253421170679"
    "82148086513282306647093844609550582231725359408128"
    "48111745028410270193852110555964462294895493038196"
)

# Cone dimensions
r = Decimal("5")   # radius
h = Decimal("10")  # height

places = [20, 40, 60, 80, 100]

print("Cone Volume Comparison using Truncated vs Rounded pi\n")
print("Formula: V = (1/3) * π * r² * h")
print("r = 5, h = 10\n")

for n in places:
    factor = Decimal('1.' + '0' * n)

    pi_trunc = pi.quantize(factor, rounding=ROUND_DOWN)
    pi_round = pi.quantize(factor, rounding=ROUND_HALF_UP)

    volume_trunc = (Decimal("1") / Decimal("3")) * pi_trunc * r**2 * h
    volume_round = (Decimal("1") / Decimal("3")) * pi_round * r**2 * h

    difference = abs(volume_round - volume_trunc)

    print(f"Decimal places: {n}")
    print(f"Volume (Truncated π): {volume_trunc}")
    print(f"Volume (Rounded π)  : {volume_round}")
    print(f"Difference          : {difference}")
    print("-" * 70)
