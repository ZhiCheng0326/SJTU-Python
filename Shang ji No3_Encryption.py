def main2():
    x = raw_input("Please enter a string:")
    y = input("Please input a number:")
    list = []
    for i in x:
        if 65 <= ord(i)+ y <= 90 or 97 <= ord(i) + y <= 122:
            list.append(chr(ord(i) + y))
            
        elif (65 <= ord(i) <= 90) and (65 > ord(i)+ y or ord(i)+ y > 90):
            list.append(chr(ord(i) + y - 90 + 65 - 1))
            
        elif (97 <= ord(i) <= 122) and (97 > ord(i)+ y or ord(i)+ y > 122):
            list.append(chr(ord(i) + y - 122 + 97 - 1))
            
        else:
            print "Error"
            
    print ''.join(list)

main2()
