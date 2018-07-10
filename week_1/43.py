while True:
    n=input()
    if n == '-1':
        break
    elif n == '0':
        continue
    else :
        last = int(n , 2)
        now = 888
        ans = 0
        while True:
            if last == 0 or last == 1:
                break
            elif last % 2 == 0 :
                last /= 2
            elif last % 2 == 1:
                last = (last+1)/2
            ans += 1
    if ans == '0b0':
        print('0000')
    else:
        print(bin(ans)[-4:].replace('b','0').zfill(4))