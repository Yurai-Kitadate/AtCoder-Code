N = int(input())
A = []
for i in range(N):
  A.append(list(map(int,input().split())))
C = 1
for i in range(N):
  C *= sum(A[i])
  C %= 10**9 + 7
print(C)
#よく考えると一回で出るsumの積になる
