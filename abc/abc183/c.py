#全探索 itertools
import itertools
N,K=map(int,input().split())
t=[0]*N

for i in range(N):
    t[i]=list(map(int,input().split()))
moto=[]
for i in range(2,N+1):
    moto.append(i)
# print(moto)
# basyo=[0]*(N+1)
# for i in range(N+1):
#     basyo[i]=moto


p=list(itertools.permutations(moto,N-1))

wa=0
ans=0
for i in p:
    mae=1
    wa=0

    for j in i:

        wa=wa+t[mae-1][j-1]

        mae=j
    if(t[j-1][0]+wa==K):
        ans=ans+1

print(ans)
