def main():
    x = raw_input("Please enter:")
    a = 0
    b = 0
    if ord(x[0])==95 or 65 <= ord(x[0]) <= 90 or 97 <= ord(x[0]) <= 122:
        a = 0
    else:
        a = 1

    for i in range(1,len(x)):
        if ord(x[i])==95 or 65 <= ord(x[i]) <= 90 or 97 <= ord(x[i]) <= 122 or 48 <= ord(x[i]) <= 57:
            b = 0
        else:
            b = 1

    if a + b != 0:
        print "invalid"
    else:
        print "valid"
main()
