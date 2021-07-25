Q = int(input())
tx = []
for i in range(Q):
  tx.append(list(map(int,input().split())))
from collections import deque
E = deque()
for i in range(Q):
  if tx[i][0] == 1:
    E.appendleft(tx[i][1])
  elif tx[i][0] == 2:
    E.append(tx[i][1])
  else:
    print(E[tx[i][1]-1])
  #dequeを使って左右に回すだけ
