#array creation
import numpy as np

#2d array
# a=np.array([[1,2,3],[2,3,4]])
# print(a)

#array datatype
# arr=np.array([1,2,3,4],dtype=
#              np.int32)
# print(arr.dtype)
# print(arr.shape)
# print(arr.size)
# print(arr.ndim)

# arr=np.array([[1,2,3,4],
#               [2,3,4,5]])
# e=arr[0:1,1:2]
# print(e)


# dtype = [('name', 'S10'), ('age', 'i4')]
# data = np.array([('Mark', 25), ('Jobin', 30)], dtype = dtype)
# print(data)
# print(type(data))


# class A:   
#     print("hi")
#     def fun1(self):
#         print("Sudip")
#     def fun2():
#         print("Bye")
# a=A()
# a.fun1()
# a.fun2()

#Generation of random matrix number .

rng = np.random.default_rng()
a=rng.integers(10,size=(3,4))
print(a)



# r=np.random.randn(2,10)*10
# print(r)
# p=np.diag([1,2,3,4,5])
# print(p)

# a=np.ones((2,3))
# a=np.eye(3)
# print(a)
