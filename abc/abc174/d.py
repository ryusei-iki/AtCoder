N=int(input())

c=list(input())


#c[1]=c[2]
sta=1
ans=0
for i in range(N):
    if(-sta+N<i):
        break
    if(c[i]=='W'):
        for j in range(sta,N):
            if(-j+N<=i):
                print(ans)
                exit()
                break
            if(c[-j]=='R'):
                temp=c[-j]
                c[-j]=c[i]
                c[i]=temp
                sta=j
                ans=ans+1
                break


print(ans)
