def mySeason():
    # month and day inputs
    m = int(input("Provide a month 1-12: "))
    d = int(input("Provide a day 1-31: "))

    # checks if the day falls in Spring
    if m == 4 or m == 5 or (m == 3 and 21 <= d <= 31) or (m == 6 and 1 <= d <= 20):
        print("Spring.")

    # checks if the day falls in Summer
    elif m == 7 or m == 8 or (m == 6 and 21 <= d <= 30) or (m == 9 and 1 <= d <= 22):
        print("Summer.")

    # checks if the day falls in Fall
    elif m == 10 or m == 11 or (m == 9 and 23 <= d <= 30) or (m == 12 and 1 <= d <= 21):
        print("Fall.")

    # checks if the day falls in Winter
    elif m == 1 or m == 2 or (m == 12 and 22 <= d <= 31) or (m == 3 and 1 <= d <= 20):
        print("Winter is here.")


mySeason()
