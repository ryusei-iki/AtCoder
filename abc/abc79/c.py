S=input()

ans=0
for i in range(1<<3):
    f=S[0]
    ans=1
    for j in range(3):

        if((i>>j) & 1==1):
            ans=ans+int(S[j+1])
            f=f+'+'+S[j+1]
        else:
            ans=ans-int(S[j+1])
            f=f+'-'+S[j+1]
    print(f)
    print(ans)
    if(ans==7):
        print(f+'=7')
