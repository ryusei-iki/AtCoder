import math
N=int(input())
L=list(map(int,input().split()))

'''
ans=0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if(L[i]!=L[j]):
                if(L[i]!=L[k]):
                    if(L[j]!=L[k]):
                        ans+=1
                        print('{},{},{}'.format(i,j,k))
            else:
                break
print(ans)
'''
count=0
ss=[]
S=[0]*N
for i in range(len(L)):
    if(not (L[i] in ss)):

        ss.append(L[i])
        if(S[ss.index(L[i])]==0):
            S[ss.index(L[i])]=1
    else:

        S[ss.index(L[i])]=S[ss.index(L[i])]+1

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

ans=0
for i in range(len(ss)-2):
    for j in range(i+1,len(ss)-1):
        for k in range(j+1,len(ss)):
            if(ss[i]+ss[j]>ss[k] and ss[j]+ss[k]>ss[i] and ss[k]+ss[i]>ss[j]):
                ans=ans+S[i]*S[j]*S[k]

print(ans)
'''
print(count)
print(combinations_count(count, 3))
'''
