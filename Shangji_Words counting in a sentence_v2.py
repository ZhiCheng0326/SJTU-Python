def main():
    x = raw_input("Please enter a sentence:")
    a = 1
    for i in x:
        if i == " ":
            a+=1
    print a
    input()
main()
