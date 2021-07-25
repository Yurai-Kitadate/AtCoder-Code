A,B = map(int,input().split())
import math
def LCM(a,b):
  return a // math.gcd(a, b) * b
Q = LCM(A,B)
if Q > 10**18:
  print("Large")
else:
  print(Q)
#やるだけ
