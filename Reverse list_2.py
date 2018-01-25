def main():
    old_list = []
    while True:
        x = raw_input("Please input a number:")
        
        if x == "c":
            print old_list
            break
        
        else:
            print "Enter 'c' to exit!"
            old_list.append(x)
    reverse_list2(old_list)
    
    
def reverse_list2(l):
    
    new_list = []

    for i in range(len(l)):
        new_list.append(l[-1+ i * (-1)])
    print new_list

main()
