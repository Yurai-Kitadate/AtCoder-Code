N,M = map(int,input().split())
ab = []
Q = [0]*N
for i in range(M):
  a,b = map(int,input().split())
  if a > b:
    Q[a-1] += 1
  if a < b:
    Q[b-1] += 1
sum = 0
for i in range(N):
  if Q[i] == 1:
    sum += 1
print(sum)
# 各辺を見ていって、頂点番号が大きい方のカウントを+1する
# カウントが1になっている頂点を数えて出力する
