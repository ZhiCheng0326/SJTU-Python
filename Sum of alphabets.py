def main():
    a = 0
    b = 0
    x = raw_input("Please input:")
    for i in x:
        if 65 <= ord(i) <= 90:
            a += (ord(i)-64)
        elif 97<= ord(i)<= 122:
            b += (ord(i)-96)
    print a+b
    
main()
