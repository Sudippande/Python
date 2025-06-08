class Employee:
    a=1
    @classmethod
    def show(cls):
        print(cls.a)
    
    @property
    def name(self):
        return self.ename
    
    @name.setter
    def name(self,value):
        self.ename=value
    
e=Employee()
e.a=45

e.name='Sudip'
print(e.name)

e.show()
