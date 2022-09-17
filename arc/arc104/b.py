N,S=map(str,input().split())
N=int(N)
ans=0
for i in range(N-1):
    con1=0
    con2=0
    for j in range(i,N):
        if(S[j]=='A'):
            con1=con1+1
        elif(S[j]=='T'):
            con1=con1-1
        elif(S[j]=='C'):
            con2=con2+1
        else:
            con2=con2-1
        if(con1==0 and con2==0):
            ans=ans+1

print(ans)
