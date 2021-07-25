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
Q = bfs(T.index(max(T)))
print(max(Q)+1)
# 支点から幅優先探索→一番遠い点からもう一回幅優先探索
# 最後のbfsでの最長距離がグラフ全体での最長距離
