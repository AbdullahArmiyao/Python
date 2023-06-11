from math import *

def leapYear():
    year = int(input("Enter Year: "))
    if year%4==0 & year%100==0 & year%400==0:
        print("It is a LEAP YEAR!")
    else:
        print("Unfortunately it is not a leap year!")

leapYear()