def checkIfPrime():
    # number to be evaluated for divisors
    n = int(input("Provide a number: "))

    isPrime = True

    # loop that iterates from 1 to n. All possible divisors will be between 2 and n
    for i in range(2, n):
        if n % i == 0:
            # sets isPrime to false if it has a divisor
            isPrime = False
            break

    # checks status of isPrime and prints
    if isPrime == False:
        print(str(n) + " is not a prime number.")
    else:
        print(str(n) + " is a prime number.")
checkIfPrime()
