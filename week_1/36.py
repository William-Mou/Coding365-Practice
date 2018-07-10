n = list(map(int,input().split(',')))
ma = []
[ma.append([999 for i in range(n[0]+1) ] ) for j in range(n[0]+1 ) ]
for i in range(n[1]):
    m = list(map(int,input().split(',')))
    ma[m[0]][m[1]], ma[m[1]][m[0]] = m[2], m[2]
def find(now = 1, used = [i for i in range(1, n[0]+1)]):
    if len(used) == 1 : return 0
    b = used.copy()
    b.remove(now)
    return min([find(i, b) + ma[now][i] for i in b])
print(find())