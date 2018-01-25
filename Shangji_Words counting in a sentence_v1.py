import string

def main():
    x = raw_input("Please input a sentence:")
    
    b = string.count(x," ")
    
    print b + 1
main()
