a = input()
l = []
if a == '1':
    while True:
        c = input().split()
        if c[0] == '1':
            if len(l) >= 5:
                print("FULL")
                break
            l.append(c[1])
        elif c[0] == '2':
            if len(l) == 0:
                print("EMPTY")
                break
            l.pop()
        elif c[0] == '3':
            if len(l) == 0:
                print("EMPTY")
                break
            else:
                print(*l)
                break
elif a == '2':
    while True:
        c = input().split()
        if c[0] == '1':
            if len(l) >= 4:
                print("FULL")
                break
            l.append(c[1])
        elif c[0] == '2':
            if len(l) == 0:
                print("EMPTY")
                break
            l.pop(0)
        elif c[0] == '3':
            if len(l) == 0:
                print("EMPTY")
                break
            else:
                for i in range(len(l)-1):
                    print(l[i], end=' ')
                print(l[-1])
                break

