N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
for i in range(N):
  A[i] = A[i]%46
  B[i] = B[i]%46
  C[i] = C[i]%46
from collections import Counter
AA = Counter(A)
BB = Counter(B)
CC = Counter(C)
count = 0
for i in range(46):
  for j in range(46):
    for k in range(46):
      if (i+j+k)%46 != 0:
        continue
      count += AA[i]*BB[j]*CC[k]
print(count)
#剰余類の個数の積を取る三重ループを書く
