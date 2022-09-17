N,M=map(int,input().split())
s=[0]*M
c=[0]*M
for i in range(M):
    s[i],c[i]=map(int,input().split())
ans=['#' for i in range(N+1)]

for i in range(M):
    if(ans[s[i]]=='#'):
        ans[s[i]]=str(c[i])
    for j in range(i+1,M):
        if(s[i]==s[j]):
            if(c[i]!=c[j]):
                print('-1')
                exit()

if(2<=N):
    if(ans[1]=='#'):
        ans[1]='1'
    elif(ans[1]=='0'):
        print('-1')
        exit()
else:
    if(ans[1]=='#'):
        ans[1]=0
        pass
    print(ans[1])
    exit()
a=ans[1:]

a=''.join(a).replace('#','0')
print(a)
