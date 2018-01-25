def main():
    from string import *
    x = raw_input("Please enter:")
    x = lower(x)
    x = capwords(x)
    x = replace(x, ' ', '')
    for i in x:
        if "a"<= i <= "z":
            x = replace(x,i,"")
        elif "A" <= i <= "Z":
            continue
        else:
            x=replace(x,i,"")
    print x
main()
