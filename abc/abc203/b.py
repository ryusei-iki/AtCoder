n,k=map(int,input().split())
ans=0
for i in range(n):
    ans=100*(i+1)*k+(k+1)*k//2+ans
print(ans)
