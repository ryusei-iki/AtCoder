#全探索
#組合せ
s=input()
from operator import mul
from functools import reduce
import itertools
def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


lis=[0]*3
kakujitu=[]
kanou=[]
for i in range(len(s)):
    if(s[i]=='o'):
        lis[0]=lis[0]+1
        kakujitu.append(i)
        kanou.append(i)
    elif(s[i]=='x'):
        lis[1]=lis[1]+1
    elif(s[i]=='?'):
        lis[2]=lis[2]+1
        kanou.append(i)


if(4<lis[0]):
    print(0)
    exit()
if(10==lis[1]):
    print(0)
    exit()



subete=list(itertools.product(kanou, repeat=4))


check=[0]*lis[0]
ans=0

# con=0
#
# while(1):
#     print(subete[con])
#     con=con+1
#     if(con==10):
#         exit()
# print('---------------')
su=0

for i in subete:
    check=[0]*lis[0]

    for j in i:

        for k in range(len(kakujitu)):
            if(j==kakujitu[k]):
                check[k]=1
    su=su+1
    if(sum(check)==lis[0]):
        ans=ans+1

print(ans)
