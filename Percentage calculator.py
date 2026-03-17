def calculate_percentage():
    global x, x_perc_of_y, y, x_perc_of_y, perc, one_perc
    print()
    print("How much is 'x' of 'y'?")
    x = int(input("x = "))
    y = int(input("y = "))
    perc = 0
    if x<y:
        one_perc = y / 100
        x_perc_of_y = x / one_perc
        perc = x_perc_of_y
        print("'x' is", perc, end="")
        print("%", "of 'y'")
    else:
        print("Please make sure 'y' is bigger than 'x'")
    calculate_percentage()
calculate_percentage()