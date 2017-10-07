# defining function
def hurricane():
    # user input for wind speed
    wind_speed = eval(input("What is the wind speed(mph) of the hurricane?: "))

    # finding the band to place the wind speed in and printing the associated category
    if wind_speed >= 157:
        print('Hurricane is a Category 5!')
    elif wind_speed  >= 130 and wind_speed  < 157:
        print('Hurricane is a Category 4!')
    elif wind_speed  >= 111 and wind_speed  < 130:
        print('Hurricane is a Category 3!')
    elif wind_speed  >= 96 and wind_speed  < 111:
        print('Hurricane is a Category 2!')
    elif wind_speed >= 74 and wind_speed < 96:
        print('Hurricane is a Category 1!')

    # if input does not meet any of the wind bands 'default' will be printed
    else:
        print('Stay calm, this is not a hurricane.')

# calling function
hurricane()
