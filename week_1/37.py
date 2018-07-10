n = int(input())
used = [i for i in range(n)]
parent = []
for i in range(n):
    parent.append(-1)

for i in range(n-1):
    a = list(map(int, input().split()))
    parent[a[1]] = a[0]
    used.remove(a[1])
parent[used[0]] = -1
# print(parent)

for i in range(n):
    for j in range(i+1, n):
        a = i
        b = j
        ma = [-1] * n
        a_step = 1
        b_step = 1
        ma[a] = 0
        ma[b] = 0
        a1 = a
        b1 = b
        while True:
            # print(ma)
            # print(a,parent[a],b,parent[b],a_step,b_step)
            if parent[a] == -1:
                pass
            else:
                if ma[parent[a]] != -1:
                    print(a1, b1, ma[parent[a]]+ma[a]+1,sep = '-')
                    break
                else:
                    if a == used[0]:
                        pass
                    else:
                        ma[parent[a]] = a_step
                        a_step += 1
                        a = parent[a]

            if parent[b] == -1:
                pass
            else:
                if ma[parent[b]] != -1:
                    # print(ma[parent[b]],ma[b],1)
                    print(a1, b1, ma[parent[b]]+ma[b]+1,sep = '-')
                    break
                else:
                    if b == used[0]:
                        pass
                    else:
                        ma[parent[b]] = b_step
                        b_step += 1
                        b = parent[b]
        # print(a,b,ma[a]+ma[b]+1)
