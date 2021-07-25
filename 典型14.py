N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()
C = 0
for i in range(N):
  C += abs(A[i]-B[i])
print(C)
#ソートして貪欲
#左からi番目の家にはi番目に左にいる人を入れればいい(それはそう)
