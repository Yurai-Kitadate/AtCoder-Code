N = int(input())
S = input()
T = "atcoder"
DP = []
for i in range(N+1):
  DP.append([0]*8)
DP[0][0] = 1
for i in range(N):
    for j in range(8):
        DP[i+1][j] = (DP[i][j] + DP[i+1][j]) % (10**9 + 7)
        if j!=7:
            if T[j] == S[i]:
                DP[i+1][j+1] += DP[i][j]
print(DP[N][7])
