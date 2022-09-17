a,b=map(int,input().split())
ans=[]
if(a<b):
    for i in range(1,b+1):
        ans.append(-i)
    for i in range(1,a):
        ans.append(i)
    ans.append(-sum(ans))
    print(*ans)
elif(b<a):
    for i in range(1,a+1):
        ans.append(i)
    for i in range(1,b):
        ans.append(-i)
    ans.append(-sum(ans))
    print(*ans)
else:
    for i in range(1,a+1):
        ans.append(i)
        ans.append(-i)
    print(*ans)
