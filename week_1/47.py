from fractions import Fraction
n = int(input())
ma = []
ma1 = []
for row in range(n):
    n = list(map(int, input().split()))
    ma.append(n)
    ma1.append(n)
for row in range(0, len(ma)):
    for k in range(1, len(ma)):
        a = -1 * (Fraction(ma[(row+k) % len(ma)][row])/Fraction(ma[row][row]))
        for j in range(len(ma[0])):
            #print(a,row,k, j )
            #print(ma1[(row+k)%len(ma)][j], '=', str(ma[row][j]), '-1',a, ma[(row+k)%len(ma)][j])
            ma1[(row+k) % len(ma)][j] = ma[row][j] * a + ma[(row+k) % len(ma)][j]
            # print(ma1)
    ma = ma1.copy()
for row in range(len(ma)):
    print('X[{}]='.format(row+1) + str(ma[row][-1] / ma[row][row]))