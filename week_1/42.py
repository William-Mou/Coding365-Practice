k = int(input())
dp = [0, 1, 2, 4]
if k < len(dp):
    print(dp[k])
else:
    for i in range(4, k+1):
        dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    print(dp[-1])