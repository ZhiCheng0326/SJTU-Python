def main():
    i = input("Please enter the initial number:")
    f = input("Please enter the last number:")
    total = 0
    l = []
    for a in range(i,f+1):
        if a % 2 != 0:
            l.append(a)
            total += a
    print l
    print total
main()
