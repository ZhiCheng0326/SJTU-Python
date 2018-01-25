import string
def main():
    x = 0
    y = -1
    a = raw_input("Please enter a sentence:")
    while a[x] == "*":
        x = x+1
    while a[y] == "*":
        y = y-1
    b = string.replace(a[x:y+1], "*", "")
    final = a[0:x] + b + a[y+1:]

    print final
main()
