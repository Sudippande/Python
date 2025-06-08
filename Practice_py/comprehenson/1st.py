#set
# se={len(word) for word in ['apple','ball','cat','apple']}
# print(se)

#simple
# syntax(expression :valu for item in iterable if)
# x=[x**2 for x in range(5)]
# print(x)

#for Dictionary
# x=[{x:x**2 for x in range(5)}]
# print(x)


#nested com
# matrix=[[1,2],[2,3],[4,5]]
# x=[x for y in matrix for x in y]
# print(x)

#usinf--if-else
# x=['even' if x%2==0 else 'odd' for x in range(10)]
# print(x)

# evn=['even' if 10%2==0 else 'odd']
# print(evn)

# gen=(x**2 for x in range(5))
# print(next(gen))

#create a list pf square from 1 to 10.
# sqr=[x**2 for x in range(1,11)]
# print(sqr)

#create a list of Vowels from the string
# text="python Programming"
# vow='aeiouAEIOU'
# vo=[x  for x in text if x in vow]
# print(vo)

# words = ["apple", "banana", "cherry", "apple", "banana"]
# un={ len(x) for x in words}
# print(un)

# x={x:x**3 for x in range(1,6)}
# print(x)


# students = {"Ram": 45, "Sita": 39, "Gita": 78, "Hari": 25}
# # for y,x in students.items():
# #     if(x>=40):
# #         print(y)

# y={y:x>=40 for x in students.values()}
# print(y)

#decorators 
def greet(fx):
    def mfx(*args, **kwargs):
        print("First line Good morning ")
        fx(*args, **kwargs)
        print("last line Thank you for using this function")
    return mfx
    
@greet
def hello():
    print("Hello Wolrd !")

@greet
def add(a,b):
    print(a+b)

hello()
add(3,3)


