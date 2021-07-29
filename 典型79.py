H,W = map(int,input().split())
Q = []
for i in range(H):
  Q.append(list(map(int,input().split())))
T = []
for i in range(H):
  T.append(list(map(int,input().split())))
sum = 0
for i in range(H-1):
  for j in range(W-1):
    if Q[i][j] > T[i][j]:
      u = Q[i][j] - T[i][j]
      sum += u
      Q[i+1][j] -= u
      Q[i][j+1] -= u
      Q[i+1][j+1] -= u
      Q[i][j] -= u
    else:
      u = T[i][j] - Q[i][j]
      sum += u
      Q[i+1][j] += u
      Q[i][j+1] += u
      Q[i+1][j+1] += u
      Q[i][j] += u
if Q == T:
  print("Yes")
  print(sum)
else:
  print("No")
#端から0になるまで操作していく
#右下端に到達した段階まで操作を繰り返すことで可能か判定
  
