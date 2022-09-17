#@

N,X=map(int,input().split())
S=input()
ans=X
for i in S:

    if(i=='o'):

        ans=ans+1
    else:
        if(0<=ans-1):
            ans=ans-1
        else:

            pass



print(ans)
