print()
print("This is the ratio calculator.")
print("============================================================================================                 Made by advik chaudhary")

def Ask_Numbers():
    global First_number, Second_number
    print()
    First_number = int(input("What is your first number? "))
    Second_number = int(input("What is your second number? "))

def Ratio():
    Ask_Numbers()
    
    if First_number == Second_number:
        print("1 : 1")
        Ratio()
    
    elif First_number > Second_number:
        gcd = math.gcd(First_number, Second_number)
        Final_First_ratio = First_number // gcd
        Final_Second_ratio = Second_number // gcd
        print(f"{Final_First_ratio} : {Final_Second_ratio}")
        Ratio()
    
    else:
        gcd = math.gcd(Second_number, First_number)
        Final_First_ratio = First_number // gcd
        Final_Second_ratio = Second_number // gcd
        print(f"{Final_First_ratio} : {Final_Second_ratio}")
        Ratio()

import math
Ratio()