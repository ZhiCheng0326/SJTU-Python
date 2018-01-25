class Complex:
    def __init__(self,a,b):
        self.a = float(a)
        self.b = float(b)

    def __str__(self):
        if self.a == 0 and self.b == 0:
            return "0"
        elif self.b == 0:
            return "%f" % (self.a)
        elif self.a ==0:
            return "%.1fj" % (self.b)
        elif self.b < 0:
            return "%.1f%.1fj" % (self.a,self.b)
        else:
            return '%.1f+%.1fj' % (self.a,self.b)

    def __add__(self,other):
        result = Complex(self.a + other.a,self.b + other.b)
        return result

    def __sub__(self,other):
        result = Complex(self.a - other.a,self.b - other.b)
        return result

    def __abs__(self):
        result = Complex((self.a ** 2 + self.b **2)**0.5,0)
        return result

    def __mul__(self,other):
        result = Complex((self.a * other.a)-(self.b * other.b),(self.a * other.b)+(self.b * other.a))
        return result

    def __div__(self,other):
        result = Complex((self.a * other.a + self.b * other.b)/(other.a **2 + other.b **2) , (self.b * other.a - self.a * other.b)/(other.a **2 + other.b **2))
        return result

complex1=Complex(1,2)
complex2=Complex(2,-3)
complex3=Complex(2,0)
complex4=Complex(0,2)
complex5=Complex(0,0)

print complex1, abs(complex1)
print complex2, abs(complex2)
print complex3, abs(complex3)
print complex4, abs(complex4)
print complex5, abs(complex5)
print complex1+complex2
print complex1-complex2
print complex1*complex2
print complex1/complex2
