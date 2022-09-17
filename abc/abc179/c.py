#全探索
N=int(input())
ans=0
an=0
for i in range(1,int(N/2+1)):
    for j in range(i,N):
        if(i*j<N):
            if(i!=j):
                ans=ans+1
            else:
                an=an+1
            #print(i,j)


        else:
            break
print(ans*2+an)
