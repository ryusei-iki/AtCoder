#全探索
n=int(input())
if(n==1):
    print(1)
    exit()
ans=0
dame=0
for i in range(1,n):
    kari=n/i
    if(dame==2):
        break
    for j in range(i,n):
        kari_kari=kari/j
        if(kari_kari<j):
            dame=dame+1
            break
        else:
            dame=0
            ans=ans+int(kari_kari)-(j-1)
print(ans)
