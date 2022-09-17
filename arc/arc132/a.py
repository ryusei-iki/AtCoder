#@
n=int(input())
rr=list(map(int,input().split()))
cc=list(map(int,input().split()))
q=int(input())
r=[0]*q
c=[0]*q
for i in range(q):
    r[i],c[i]=map(int,input().split())
ans=''
for i in range(q):
    if(rr[r[i]-1]+cc[c[i]-1]>=n+1):
        ans=ans+'#'
    else:
        ans=ans+'.'
print(ans)
