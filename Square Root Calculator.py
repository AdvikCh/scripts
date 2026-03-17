print()
print("This is the Square Root calculator.")
print("============================================================================================                                 Made by advik chaudhary")

square_root_found = False

def Calculate_root():
    global Factor, Number, square_root_found

    while square_root_found == False:
#         if Factor <= (Number / 2) and Factor >= ((Number / 4) * 1):
        if Factor <= ((Number / 4) * 3) and Factor >= ((Number / 4) * 1):
            if (Number / Factor) == Factor:
                square_root_found = True
                print("The square root of", Number, "is", Factor)
                Number = 0
                Factor = 0
                square_root_found = True
                Square_input()
            else:
                print(Factor)
                Factor = Factor - 0.1
        else:
            print("Failed to find root")
            Square_input()
            return

def Square_input():
    global Factor, Number
    print()

    Number = int(input("What is your number? "))
    
    if Number == 1:
        print("The square root of 1 is 1")
        Square_input()
    elif Number < 0:
        print("Negative numbers have no square root")
        Square_input()
    elif Number == 0:
        print("0 has no square root")
        Square_input()
    else:
        Factor = Number / 2
        print(Factor)
        Calculate_root()

Square_input()