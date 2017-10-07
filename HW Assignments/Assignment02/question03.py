def calcFib():
    # user's term
    n = int(input("Provide a term of the Fibonacci Sequence: "))

    # starting values of 0 and 1
    now = 1
    past = 0

    # loop that iterates one less than term requested
    for i in range(1, n):
        # simultaneous assignment to successfully store previous values
        now, past = now + past, now
    print(now)
calcFib()
