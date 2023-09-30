a = list(input("Enter the postfix expression: ").split(" "))
stack = []
for i in a:
    if(len(stack)==1 and i==a[-1]):
        stack[0]= -stack[0]
        break
    if(i in ["+", "-", "*", "/"]):
        b = stack.pop()
        c = stack.pop()
        if(i=="+"):
            stack.append(c+b)
        elif(i=="-"):
            stack.append(c-b)
        elif(i=="*"):
            stack.append(c*b)
        elif(i=="/"):
            stack.append(c/b)
    elif i==" ":
        continue
    else:
        stack.append(int(i))
print("The result of the expression: ",stack[0])