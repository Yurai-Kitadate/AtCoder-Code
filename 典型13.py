v,e = map(int, input().split())
# adj[s]: ノード s に隣接する(ノード, 重み)をリストで持つ
adj = [[] for _ in range(v)]
for i in range(e):
    s, t, d = map(int, input().split())
    s -= 1
    t -= 1
    adj[s].append((t, d))
    adj[t].append((s, d))
PP = list(adj)
from heapq import heappush, heappop
INF = 10 ** 9
def dijkstra(s, n): # (始点, ノード数)
    dist = [INF] * n
    hq = [(0, s)] # (distance, node)
    dist[s] = 0
    seen = [False] * n # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1] # ノードを pop する
        seen[v] = True
        for to, cost in adj[v]: # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist
QQ = dijkstra(0, v)
adj = list(PP)
#print(PP)
QQQ = dijkstra(v-1, v)
#print(QQ)
#print(QQQ)
for i in range(v):
  print(QQ[i] + QQQ[i])
#1から他の頂点への最短距離をダイクストラで求める
#nから他の頂点への最短距離をダイクストラで求める
#ループを0から回していって、dist(1-?)[i] + dist(N-?)[i]がi番目の頂点を経由して1からNへ移動する最短距離となる。
