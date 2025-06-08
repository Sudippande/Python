# def sum(a: int,b: int) ->int:
#     return(a+b)
# a=sum(2,3,)
# print(a)

# def name(c:str)->str:
#     return c
# c=name(7)
# print(type(c))

from typing import List,Tuple,Dict,Union

def fun():
#list integers
    numbers:List[int]=[1,2,3,4]

    #tuple
    persion:Tuple[str,int]={"Sudip",12}
    #Dict
    scores:Dict[str,int]={"name":45}

    led:Union[int,str]='ID123'
    return numbers,persion,scores,led
print(fun(),"\n")