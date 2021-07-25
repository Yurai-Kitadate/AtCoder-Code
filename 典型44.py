N,Q = map(int,input().split())
A = list(map(int,input().split()))
from collections import deque
A = deque(A)
#print(A)
for i in range(Q):
  #print(A)
  t,x,y = map(int,input().split())
  if t == 2:
    P = A.pop()
    A.appendleft(P)
  elif t == 1:
    A[x-1],A[y-1] = A[y-1],A[x-1]
  else:
    print(A[x-1])
  #dequeを使うだけ
