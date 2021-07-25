N,K = map(int,input().split())
Q = []
for i in range(N):
  a,b = map(int,input().split())
  Q.append(b)
  Q.append(a-b)
Q.sort()
Q = Q[len(Q)-K:]
print(sum(Q))
#半完と全完をそれぞれ配列にいれる
#大きい方からK個を貪欲にとる
