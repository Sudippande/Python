#wite a  program that converts the list of integer to set
# a=[1,2,3,4,5]

# print(type(a))
# b=set(a)
# c=tuple(b)
# print(b)
# print(type(b))
# print(c)
# print(type(c))

#write a program that read a string and write it to another file
with open("sudip.txt",'r') as fp:
    content=fp.read()
    print(content)
with open("pande.txt",'w') as f:
    f.write(content)
    print("Successfully")
