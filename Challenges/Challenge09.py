def myFib():
    print("Fibonacci Sequence!")
    n = eval(input("Provide a whole number: "))

    now = 1
    past = 0
    for i in range(n):
        now, past = now + past, now
        print(now)


myFib()
