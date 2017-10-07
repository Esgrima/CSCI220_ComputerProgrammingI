def myDivisors():
    # number to be evaluated for divisors
    n = int(input("Provide a number: "))

    # loop that iterates from 1 to n. All possible divisors will be between 1 and n.
    for i in range(1, n + 1):
        # determines if 'i' is a divisor(result = 0) of n and prints 'i' if it is
        if n % i == 0:
            print(i)


myDivisors()
