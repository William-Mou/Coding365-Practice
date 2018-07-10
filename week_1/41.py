tree = {"first":['null']}
roots = []
not_root = []
global first
first = "first"
def printf(root = first):
    #print(root)
    tree[root] = sorted(tree[root])
    if root == "first":
        pass
    elif root == first:
        print(root,end = "")
    for j in tree[root]:
        print(j,end ="")
        if j in tree:
            printf(j)

def insert(leaf):
    for i in range(len(leaf)):
        if i == 0:
            root = leaf[i]
            #roots.append(root)
            if root in tree:
                for j in range(1,len(leaf)):
                    tree[root].append(leaf[j])
                break
            else:
                tree[root] = []
        else:
            tree[root].append(leaf[i])
            #not_root.append(i)
    return 0

flag = True
           
while True:
    #print(tree)
    n = input()
    if n == 'p':
        printf(first)
        print()
    elif n == 'i':
        leaf = input()
        if flag == True:
            first = leaf[0]
            flag = False
            #print(first)
        insert(leaf)
    else :
        break