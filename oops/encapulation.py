# This is done with the help of access modifiers,
# public variable or insstance, private(__),protected(_)
class std:
    def __init__(self,name="sudip"):
         self.__name = name
    def info(self):
         return self.__name
s1=std()
print(s1.info())
print(s1._std__name)




