N = int(input())
pattern = []
for i in range(2 ** N):
    tmp = [False] * (N)
    for j in range(N):
        if i >> j & 1:
            tmp[j] = True
    pattern.append(tmp)
#print(pattern)
W = []
PPP = []
for i in range(len(pattern)):
  PP = ""
  count = 0
  C = 0
  for j in range(N):
    if pattern[i][j]:
      PP += "("
      count += 1
    else:
      PP += ")"
      count -= 1
    if count < 0:
      C = 1
      break
  if C == 1:
    continue
  if count == 0:
    PPP.append(PP)
PPP.sort()
for i in range(len(PPP)):
  print(PPP[i])
# bit全探索で()の並びを全列挙する
# sortして順番に出力
