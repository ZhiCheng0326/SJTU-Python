def main():
    x = raw_input("Please input a series of number:")
    c = 0
    l = []

    for i in range(len(x)):
        if i+1 <= len(x)-1 and x[i] != x[i+1]:
            c += 1
            l.append(i)
    print l
    for i in l:
        a = 1
        b = 2
        while x[i-a] == x[i] and x[i+b] == x[i+1]:
            c +=1
            a +=1
            b +=1
    print "The number of sets: ",c
main()
