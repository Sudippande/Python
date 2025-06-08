# abstact
from abc import ABC,abstractmethod
class demo(ABC):
    @abstractmethod
    def fun1(self):
        print("Hello this is a first one.")
    def fun2(self):
        print("This is fun 2")
    def fun3(self):
        print("this is a fun 3")
class Dem(demo):
    def fun1(self):
        super().fun1()
        return
ob=Dem()
ob.fun1()
ob.fun2()
ob.fun3()