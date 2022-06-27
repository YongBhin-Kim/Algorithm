# 1,2,3 더하기

# n : 1~10

# n=1 -> (1) (1가지)
# n=2 -> (1+1) (2) (2가지)
# n=3 -> (1+1+1) (1+2) (2+1) (3) (4가지)
# n=4 -> (1+1+1+1) (1+1+2) (1+2+1) (2+1+1) (2+2) (1+3) (3+1) (7가지)
# n=5 -> 1+1+1+1+1 1+1+1+2 1+1+2+1 1+2+1+1 2+1+1+1 1+2+2 2+1+2 2+2+1 1+1+3 1+3+1 3+1+1 2+3 3+2 (13가지)
# dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

dp = [0]*11
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4,11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
t = int(input()) 
for _ in range(t):
    n = int(input())
    print(dp[n])
    