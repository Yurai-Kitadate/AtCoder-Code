N = int(input())
import statistics
X = []
Y = []
for i in range(N):
  x,y = map(int,input().split())
  X.append(x)
  Y.append(y)
X.sort()
Y.sort()
medX = statistics.median(X)
medY = statistics.median(Y)
C = 0
for i in range(N):
  C += abs(medX-X[i])
  C += abs(medY-Y[i])
import math
print(math.floor(C))
#x,y独立に考える
#両方ともそれぞれの中央値を考えればよい
