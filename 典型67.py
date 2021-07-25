def DeciamlToNine(num):
    "10進数を9進数に変換する"
    nine_number = ""
    while num > 0:
        nine_number += str(num % 9)
        num //= 9
    return int(nine_number[::-1])
N,K = map(int,input().split())
if N == 0:
  print(0)
  exit()
for i in range(K):
  N = str(N)
  N = int(str(N), 8)
  N = DeciamlToNine(N)
  N = list(str(N))
  Q = ""
  for j in range(len(N)):
    if N[j] == "8":
      Q += "5"
    else:
      Q += N[j]
  N = int(Q)
print(N)
#問題文に沿ってやるだけ。n進数をr進数に変換する方法がわかれば大丈夫
