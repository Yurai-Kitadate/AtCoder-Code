H,W = map(int,input().split())
import math
if H == 1 or W == 1:
  print(H*W)
  exit()
print(math.ceil(H/2)*math.ceil(W/2))
#コーナーケースに注意😠
