N = int(input())
import itertools
ls = list(itertools.permutations(range(0,N)))
A = []
for i in range(N):
  A.append(list(map(int,input().split())))
M = int(input())
XY = []
for i in range(N):
  XY.append([True]*N)
for i in range(M):
  x,y = map(int,input().split())
  x -= 1
  y -= 1
  XY[x][y] = False
  XY[y][x] = False
#print(ls)
Q = []
for i in range(len(ls)):
  cnt = 0
  pp = 0
  for j in range(N):
    cnt += A[ls[i][j]][j]
    if j >= 1:
      if XY[ls[i][j-1]][ls[i][j]] == False:
        break
    pp += 1
  if pp == N:
    Q.append(cnt)
if Q == []:
  print(-1)
else:
  print(min(Q))
#順列全探索をする
