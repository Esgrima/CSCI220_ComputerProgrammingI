import statistics


def exam_average():
    print("This function computes the average of three exam grades.")
    exam1, exam2, exam3 = eval(input("What is the grade of the 1st exam?(I: "))

    average = round(statistics.mean([exam1, exam2, exam3]), 2)

    print("Your exam average is " + str(average) + '.')
exam_average()
