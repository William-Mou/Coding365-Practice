l = []
while True:
    n = input()
    if n == 'e':
        break
    elif n == 'p':
        if len(l) == 0:
            print('null')
        else:
            print(*l)
    elif n == 'i' :
        a = int(input())
        l.append(a)
        l.sort()
