H,W = map(int,input().split())
A = []
B = []
for i in range(H):
  A.append(list(map(int,input().split())))
  B.append(sum(A[i]))
C = []
S = 0
for j in range(W):
  for i in range(H):
    S += A[i][j]
  C.append(S)
  S = 0
AAA = []
SSS = []
for i in range(H):
  for j in range(W):
    SSS.append(B[i] + C[j] - A[i][j])
  AAA.append(SSS)
  SSS = []
for i in range(H):
  print(*AAA[i])
 # 行の和と列の和をそれぞれ計算
 # A[i][j]をダブルカウントしているので引く
