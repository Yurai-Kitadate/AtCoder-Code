N,K = map(int,input().split())
a = list(map(int,input().split()))
Dic = dict()
LONG = 0
head = 0
tail = 0
while True:
  if head == N:
    break
  if a[head] in Dic:
    Dic[a[head]] += 1
  else:
    Dic[a[head]] = 1
  head += 1
  if len(Dic) > K:
    while len(Dic) > K:
      if Dic[a[tail]] >= 2:
        Dic[a[tail]] -= 1
      else:
        Dic.pop(a[tail])
      tail += 1
  else:
    LONG = max(LONG,head - tail + 1)
print(LONG-1)
#尺取り法?を使う
#K以下での範囲の長さとLONGのmaxをとってあげればよい
