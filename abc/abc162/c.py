K=int(input())
import math
out=0

for i in range(1,K+1):
    for j in range(1,K+1):
        for k in range(1,K+1):
            out=out+math.gcd(i,math.gcd(j,k))
print(int(out))
