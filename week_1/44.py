while True:
    n=input()
    if n == '-1':
        break
    elif n == '0':
        continue
    else :
        lasts = int(n , 2)
        ans = 0
        for last in range(lasts+1): 
            while True:
                if last == 0 or last == 1:
                    break
                elif last % 2 == 0 :
                    last /= 2
                elif last % 2 == 1:
                    last = (last+1)/2
                ans += 1
        #print("*", last ,ans)
    #print(ans)
    if ans == '0b0':
        print('00000000')
    else:
        print(bin(ans)[-11:].replace('b','0').zfill(11))