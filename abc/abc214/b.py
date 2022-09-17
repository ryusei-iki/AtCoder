#全探索
s,t=map(int,input().split())
ans=0
for i in range(max(s,t)+1):
    for j in range(max(s,t)+1):
        if(s-i-j<0):
            break
        if(i==0 or j==0):
            ans=s-i-j+1+ans
        else:
            ans=min(s-i-j+1,t//(i*j)+1)+ans

print(ans)






