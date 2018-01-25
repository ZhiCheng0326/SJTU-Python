def slope(p1,p2):
    gradient = (p2[1]-p1[1])/float(p2[0]-p1[0])
    return gradient

def intercept(p1,p2):
    gr=slope(p1,p2)
    c = p1[1] - (gr * float(p1[0]))
    return c

def main2():
    x1,y1 = input("Please input x1-coordinate and y1-coordinate:")
    x2,y2 = input("Please input x2-coordinate and y2-coordinate:")
    p1 =(x1,y1)
    p2 =(x2,y2)
    slope(p1,p2)
    intercept(p1,p2)
    print "Slope is ", round(slope(p1,p2),2)
    print "The y-intercept is ", round(intercept(p1,p2),2)

main2()
    
    
    


    
