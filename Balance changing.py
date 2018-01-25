def main():
    x = input("Please enter price:")
    a,b,c,d,e,f = 0,0,0,0,0,0
    
    change = 1.0 - x
    change = round(change,2)
    while change > 0.00:
        if change >= 0.5:
            a += 1
            change -= 0.5
            change = round(change,2)
        elif change >= 0.2:
            b += 1
            change -= 0.2
            change = round(change,2)
        elif change >= 0.1:
            c += 1
            change -=0.1
            change = round(change,2)
        elif change >= 0.05:
            d += 1
            change -= 0.05
            change = round(change,2)
        elif change >= 0.02:
            e +=1
            change -=0.02
            change = round(change,2)
        elif change <= 0.01:
            f +=1
            change -= 0.01
            change = round(change,2)
    print a, b, c, d, e, f
  
main()
