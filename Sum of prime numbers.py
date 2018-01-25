def main():
    "Input : An integer n"
    "Output: The sum of all prime number from 1 to n."

    n = input("Please enter an integer:")
    l = [2]
    prime = 0
    plus = 0
    for i in range(3,n+1):
        prime = True
        for j in range(2,i):
            if i%j == 0:
                prime = False
        if prime == True:
            l.append(i)
    print l

    for k in l:
        plus += k
    print plus
main()
