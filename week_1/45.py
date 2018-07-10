def g(n, k):
    if n == 1:
        return str(k)
    elif k < 2 ** (n-1):
        return '0' + g(n-1, k)
    else:
        return '1' + g(n-1, 2**n-1-k)

while True:
    n,k = map(int, input().split())
    print(g(n, k))
    q = input()
    if q == '-1':
        break