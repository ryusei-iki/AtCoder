ビット全探索
s=input()

n=len(s)-1
ans=0
for i in range(2**n):
    mae=0
    for j in range(n):
        if((i>>j)&1):
            ans=ans+int(s[mae:j+1])

            mae=j+1

    ans=ans+int(s[mae:])

print(ans)
