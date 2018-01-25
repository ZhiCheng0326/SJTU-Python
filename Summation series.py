def main():
    x = input("Please input a digit:")
    list1= []
    for i in range(1,x+1):
        a = i ** i
        list1.append(a)
    print list1
    for j in list1:
        number = str(j)
        print number + " " + "+",
main()
