# P 前序： 中左右
# I 中序： 左中右
# O 後序： 左右中
global tree
tree = []
global q
q = []
l = ['i', 'p', 'o']
for _ in range(2):
    n = input()
    k = input()
    #print(n,k)
    if n == 'I':
        i = []
        for j in k:
            i.append(j)
        l.remove('i')
    if n == 'P':
        p = []
        for j in k:
            p.append(j)
        l.remove('p')
    if n == 'O':
        o = []
        for j in k:
            o.append(j)
        l.remove('o')

def sortp(p, i):
    #print(p,i)
    if len(i) == 0:
        return
    elif len(i) == 1:
        tree.append(i[0])
        return
    tree.append(p[0])
    for j in range(len(i)):
        #print(i[j], p[0])
        if i[j] == p[0]:
            i1 = i[:j]
            i2 = i[j+1:]
            len_i1 = len(i1)
            break
    #print(p)
    p1 = p[1:len_i1+1]
    p2 = p[len_i1+1:]
    #print(p1 ,i1)
    #print(p2 ,i2)
    q.append([p1, i1])
    q.append([p2, i2])


def sorto(o, i):
    if len(i) == 0:
        return
    elif len(i) == 1:
        tree.append(i[0])
        return
    
    tree.append(o[-1])
    for j in range(len(i)):
        if i[j] == o[-1]:
            i1 = i[:j]
            i2 = i[j+1:]
            len_i2 = len(i2)
            break   
    o1 = o[0:-1 * len_i2 -1 ]
    o2 = o[-1 * len_i2 -1 : -1]
    #print(o1,i1)
    #print(o2,i2)
    q.append([o1, i1])
    q.append([o2, i2])

if 'o' in l:
    q.append([p, i])
    while len(q) != 0:
        # print(q)
        p, i = q.pop(0)
        sortp(p, i)
        # print(tree)
else:
    q.append([o, i])
    while len(q) != 0:
        o, i = q.pop(0)
        sorto(o, i)

print(*tree, sep="")
print()