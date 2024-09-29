def push(stack,tmp):
    stack.append(tmp)

def pop(stack):
    if(len(stack)==0):
        print("overflow")
    return stack.pop()

def insertatbottom(stack,tmp):
    if(len(stack)==0):
        push(stack,tmp)
    else:
        temp = pop(stack)
        insertatbottom(stack,tmp)
        push(stack,temp) 

def reverse_stack(stack):
    if(len(stack)!=0):
        temp = pop(stack)
        reverse_stack(stack)
        insertatbottom(stack,temp)

stack = [3,3,3]
reverse_stack(stack)
print(stack)
        