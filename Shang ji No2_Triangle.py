#No 2
def main():
    x = input("Please enter side1:")
    y = input("Please enter side2:")
    z = input("Please enter side3:")

    p = (x + y + z)/2
    a = x + y + z
    w = (p * (p-x) * (p-y) * (p-z)) ** 0.5

    if (x + y >= z) or (x + z >= y) or (y + z >= x):
        print "The perimeter is" , a
        print "The area is", w
    else:
        print "Invalid"
main()
