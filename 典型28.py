N = int(input())
Q = [[0]*2000 for i in range(2000)]
for i in range(N):
    lx,ly,rx,ry = map(int, input().split())
    Q[lx][ly] += 1
    Q[rx][ly] -= 1
    Q[lx][ry] -= 1
    Q[rx][ry] += 1
res = [0]*(N+1)
for j in range(2000):
    l = [0]*2000
    for i in range(2000):
        if j != 0:
            Q[j][i] += Q[j-1][i]
        l[i] = l[max(0,i-1)] + Q[j][i]
        res[l[i]] += 1
for i in range(1,N+1):
    print(res[i])
#二次元いもす法を考える。角に判定を加えてx,y方向に引き伸ばす
#k枚重なっているところをそれぞれ数えていく
