class Triangle:
    def __init__(self,p1,p2,p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        
    def isInside(self,p4):
        x1,y1 = self.p1[0],self.p1[1]
        x2,y2 = self.p2[0],self.p2[1]
        x3,y3 = self.p3[0],self.p3[1]
        x4,y4 = p4[0],p4[1]
        
        self.area = float(0.5 * abs((x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3)))
        area1 = float(0.5 * abs((x4*y2+x2*y3+x3*y4)-(x2*y4+x3*y2+x4*y3)))
        area2 = float(0.5 * abs((x1*y4+x4*y3+x3*y1)-(x4*y1+x3*y4+x1*y3)))
        area3 = float(0.5 * abs((x1*y2+x2*y4+x4*y1)-(x2*y1+x4*y2+x1*y4)))
        
        if area1 + area2 + area3 == self.area:
            print True
        else:
            print False

        
triangle1=Triangle((-4,0),(4,0),(0,8))
triangle1.isInside((4,8))
triangle1.isInside((0,0))
triangle1.isInside((2,4))

triangle2=Triangle((-1,-1),(2,1),(4,10))
triangle2.isInside((3,5.5))
triangle2.isInside((0,0))                   
triangle2.isInside((4,9))
