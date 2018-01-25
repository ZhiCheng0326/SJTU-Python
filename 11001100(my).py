def main():
    x = raw_input("Please input a series of number:")
    c=0

    for i in range(len(x)):
        a = 1
        b = 1
        d = 1
        while i+d <= len(x)-1 and x[i] == x[i+d]:
            a += 1
            d += 1
        while i+d+1 <= len(x)-1 and x[i+d] == x[i+d+1]:
            b += 1
            d += 1
        if b >= a:
            #print a*x[i]
            c += 1

    print "Number of sets:", c-1
main()
