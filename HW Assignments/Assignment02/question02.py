def calcWages():
    # user input for wage and hours
    wage = float(input("What's your hourly wage?: "))
    hours = float(input("How many hours did you work this week?: "))

    # determines which equation to use based on the hours
    if 0.0 <= hours <= 40.0:
        total_wages = wage * hours
    elif hours > 40.0:
        overtime = hours - 40.0
        total_wages = (wage * 40.0) + overtime * (1.5 * wage)

    print("Total wages for the week: $" + str(total_wages))
calcWages()
