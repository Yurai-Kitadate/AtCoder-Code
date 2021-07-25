N = int(input())
C1 = [0]*N
C2 = [0]*N
for i in range(N):
  c,p = map(int,input().split())
  if c == 1:
    C1[i] = p
  else:
    C2[i] = p
Q = int(input())
sum1 = [0]*(N+1)
for i in range(N):
  sum1[i+1] = sum1[i] + C1[i]
sum2 = [0]*(N+1)
for i in range(N):
  sum2[i+1] = sum2[i] + C2[i]
#print(sum1,sum2)
for i in range(Q):
  L,R = map(int,input().split())
  print(sum1[R]-sum1[L-1],sum2[R]-sum2[L-1])
#1組、2組それぞれの累積和を取る
