N = int(input())
E = set()
for i in range(N):
  s = input()
  if s in E:
    continue
  else:
    print(i+1)
    E.add(s)
#setを使う sが既にあったらcontinue なかったら日付をprintしてsetにadd
