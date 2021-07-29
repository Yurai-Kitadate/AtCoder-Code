N,K = map(int, input().split())
cnt = [0] * (N + 1)
res = 0
for Q in range(2,N + 1):
    if cnt[Q] == 0:
        for P in range(Q,N+1,Q):
            cnt[P] += 1
    if cnt[Q] >= K:
        res += 1
print(res)
#素数だったら、倍数を塗っていく
#塗られた回数がK以上だったらres++
