#16

def main1():
    x = 999999
    value = [1, 1]
    for i in range(x-2):
        value.append(value[i] + value[i+1])
        
        if value[i+2] >= 100:
            break
    print value
    print "Therefore the value is", value[i+2]

main1()
