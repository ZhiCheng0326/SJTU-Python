def main():
    old_list = []
    while True:
        x = raw_input("Please input a number:")
        
        if x == "c":
            break
        
        else:
            print "Enter 'c' to exit!"
            a = old_list.append(x)
    
    reverse_list(old_list) 

def reverse_list(l):
    
    temp = 0
    for i in range(len(l)/2):
        temp = l[i]
        l[i] = l[-1+ i * (-1)]
        l[-1+ i * (-1)] = temp
    print l
    
main()
