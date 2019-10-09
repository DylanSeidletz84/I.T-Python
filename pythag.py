from banner import banner
from math import sqrt
banner ("Pythagorean Calculator", "Dylan Seidletz")

calculate = "Y"
while calculate == "Y" or calculate == "y":
    print('We will help you find the missing side of a right triangle. The lengths of the two')
    print("legs are 'a' and 'b', and the hypotenuse is 'c'.")
    print("")
    print("Please enter the length of each side, or leave it blank if you don't know.")
    A = input('Input the length of side a: ')
    B = input('Input the length of side b: ')
    C = input('Input the length of side c: ')
    try:
        C = int(c)
    except:
        C = None
    try:
        A = int(A)
    except:
        A = None
    try:
        B = int(B)
    except:
        B = None

    if not C:
        C = sqrt((A * A) + (B * B))
        print('The length of side c is:',(C))
        calculate = input("Would you like to calculate another triangle (Y/N)?")
    elif not A:
        A = sqrt((C * C) - (B * B))
        print('The length of side a is:',(A))
        calculate = input("Would you like to calculate another triangle (Y/N)?")
    elif not B:
        B = sqrt((C * C) - (A * A))
        print('The length of side b is:',(B))
        calculate = input("Would you like to calculate another triangle (Y/N)?")
        try:
            B = int(B)
        except:
            B = None
    else:
        print('Please select a side between a, b, c')
        calculate = input("Would you like to calculate another triangle (Y/N)?")