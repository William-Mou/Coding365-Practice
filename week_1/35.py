n = input().strip()
stack = []
xx = {'+':1,'^':3,'-':1,'*':2,'/':2,'(':10}
for i in n:
    if i == '(':
        stack.append(i)
    elif i in xx:
        if len(stack) == 0:
            stack.append(i)
        elif xx[i] <= xx[stack[-1]]:
            while xx[i] <= xx[stack[-1]]:
                if stack[-1] == '(':
                    break
                print(stack.pop(),end = '')
                if len(stack) == 0:
                    break
            stack.append(i)
        else:
            stack.append(i)
    elif i == ')':
        while stack[-1] != '(':
            print(stack.pop(),end = '')
        stack.pop()
    else:
        print(i,end = '')
while len(stack) != 1:
    print(stack.pop(),end = '')
print(stack.pop())