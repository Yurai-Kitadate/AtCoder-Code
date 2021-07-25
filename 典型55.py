N,P,Q = map(int,input().split())
A = list(map(int,input().split()))
count = 0
for i in range(N):
  for j in range(i+1,N):
    for k in range(j+1,N):
      for l in range(k+1,N):
        for r in range(l+1,N):
          if (A[i]%P*A[j]%P*A[k]%P*A[l]%P*A[r]%P)% P== Q:
            count += 1
print(count)
#迫真5重ループ(数が大きくなってTLEするのでmodを取り忘れないように)
