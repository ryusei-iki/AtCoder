n=int(input())
ans=0
for i in range(n+1):
    if(len(str(i))>=2):

        if(str(i)[0:len(str(i))//2]==str(i)[len(str(i))//2:len(str(i))]):
            print(i)
            ans=ans+1
            print(ans)
print(ans)
