stack=[]
def push():
    element=input("Enter the element :")
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("Stack is empty !")
    else:
        ele=stack.pop()
        print("Removed stack is:",ele)
        print(stack)
if __name__=='__main__':
        while True:
            print("\nOption:\n1. Push\n2. pop\n3. Exit")
            choice=input("Enter  your choice(1/2/3): ")

            if choice =='1':
                 push()
            elif choice=='2':
                 pop_element()
            elif choice =='3':
                 print("Existing program.")
                 break
            else:
                 print("Invalid choice. please try again.")