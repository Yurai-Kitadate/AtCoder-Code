N = int(input())
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        if n == 1:
          print("素数じゃない")
        else:
          arr.append([n, 1])
    return arr
Q = factorization(N)
cnt = 0
for i in range(len(Q)):
  cnt += Q[i][1]
if cnt == 1:
  print(0)
  exit()
m = 1
for i in range(10000):
  m *= 2
  if cnt <= m:
    print(i+1)
    exit()
#素数が分裂していく
#2ˆnがcntを超えるnが必要な分裂回数
