#全探索
a=list(map(int,input().split()))

lis=[0]*n
for i in range(n):
    lis[a[i]]=lis[a[i]]+1

ima=lis[0]
ans=0
ans_lis=[]
if(lis[0]==0):
    print(0)
    exit()

for i in range(1,n):
    if(lis[i]==0):
        if(ima<k):
            ans=ans+ima*(i)

            if(len(ans_lis)==0):
                pass
            else:

                ans=ans+sum(ans_lis[max(len(ans_lis)-(k-ima),0):])

            print(ans)
            exit()
        elif(ima==k):

            print(ima*(i))

            exit()
        else:

            ans=ans+k*i
            print(ans)

            exit()
    elif(lis[i]<ima):
        for j in range(ima-lis[i]):
            ans_lis.append(i)
    ima=min(lis[i],ima)
if(ima<k):
    ans=ans+ima*(i+1)
    if(len(ans_lis)==0):
        pass
    else:
        ans=ans+sum(ans_lis[len(ans_lis)-(k-ima):])
    print(ans)

elif(ima==k):

    print(ima*(i+1))

else:
    ans=ans+k*(i+1)
    print(ans)
