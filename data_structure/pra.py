def create_stk():
    stack=[]
    return stack

def stack_empty(stack):
    if stack==0:
    return len(stack) == 0

#push 
def push(stack,items):
    stack.append(items)
    print("Pushed item is:",items)

#pop
def pop(stack):
    if (stack_empty()):
        return "stack is empty"
    return stack.pop()


stack=create_stk()
push(stack,str(1))
push(stack,str(2))
push(stack,str(3))
push(stack,str(4))
push(stack,5)
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))