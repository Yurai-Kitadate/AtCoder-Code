import sys
N = int(input())
g = [[] for _ in range(N)] # 隣接リスト
for _ in range(N-1):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
from collections import deque
def bfs(u):
    queue = deque([u])
    d = [None] * N # uからの距離の初期化
    d[u] = 0 #oad") 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d
T = bfs(0)
#print(T)
QQQ = []
PPP = []
for i in range(N):
  if T[i] % 2 == 0:
    QQQ.append(i+1)
  else:
    PPP.append(i+1)
if len(QQQ) >= len(PPP):
  print(*QQQ[:N//2])
else:
  print(*PPP[:N//2])
#距離の偶奇が等しい頂点同士は必ず隣り合っていない
#距離が偶数の頂点or奇数の集合が大きい方を出力する
