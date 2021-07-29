from collections import deque
c = deque()
N = int(input())
A = list(map(int,input().split()))
Q = sum(A)
A = A+A
cnt = 0
for i in range(2*N):
  c.append(A[i])
  cnt += A[i]
  if cnt == Q/10:
    print("Yes")
    exit()
  if cnt > Q/10:
    t = c.popleft()
    cnt -= t
print("No")
#両端同士は繋がっているので二周回してあげる
#0.1より小さければ追加していき、大きければ最後尾を引く
