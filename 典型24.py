N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
sum = 0
for i in range(N):
  sum += abs(A[i]-B[i])
if sum == K:
  print("Yes")
elif K >= sum and (K-sum)%2 == 0:
  print("Yes")
else:
  print("No")
#理想からの差と操作回数が同じならYes
#理想からの距離より操作回数が多くて操作回数と理想からの距離の和が偶数なら、同じ箇所を+-することで時間を稼げるのでYes
#それ以外はNo
