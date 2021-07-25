N,L = map(int,input().split())
DP = [0]*(N+1)
DP[0] = 1
for i in range(1,N+1):
  if i - L >= 0:
    DP[i] = DP[i-1] + DP[i-L]
    #print(DP[i])
  else:
    DP[i] = DP[i-1]
    #print(DP[i])
print(DP[N]%(10**9+7))
#flogです
