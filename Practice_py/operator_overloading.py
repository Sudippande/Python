class vector:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    
    def __str__(self):
            return f"{self.a}a+{self.b}b+{self.c}c"
    
    def __add__(self,x):
         return vector(self.a  +x.a, self.b + x.b, self.c + x.c)
abc=vector(3,4,5)
bcd=vector(4,5,6)
print(abc)
print(bcd)
print(abc+bcd)