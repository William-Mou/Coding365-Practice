n = int(input())
ma = []
dire = [(1,0),(-1,0),(0,-1),(0,1)]
for i in range(n):
    m = input().split()
    ma.append(m)
#print(ma)

def find(now, used):
    if now == (n-2,n-2):
        used.append((n-2,n-2))
        return used
    for i in dire:
        #print("now" , now)
        #print("i", i)
        #print("next",ma[ now[0] + i[0]][ now[1] + i[1]])
        #print(used)
        next_point = ma[ now[0] + i[0]][ now[1] + i[1]]
        #print(next_point)
        if next_point != '1' :
            if (now[0] + i[0], now[1] + i[1]) in used:
                pass
            else:
                used.append(now)
                used1 = used.copy()
                ans = find((now[0]+i[0],now[1]+i[1]),used1)
                if ans != False:
                    return ans
    return False 
     
point = find((1,1),[])
#print(point)

for i in point:
    ma[i[0]][i[1]] = '#'
for i in ma:
    print(*i)