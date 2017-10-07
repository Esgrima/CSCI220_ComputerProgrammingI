# importing fraction function
from fractions import Fraction


def series():
    n = int(input("Provide a 'n' term of the ((3n + 1)/ 3**n) series: "))
    total = 0

    # loop that runs n times
    for i in range(1, n + 1):
        seriesSum = ((3 * i) + 1) / 3 ** i
        # total += seriesSum
        print(Fraction(seriesSum).limit_denominator(), end=" + ")
series()

