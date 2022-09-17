#文字コード
p=list(map(int,input().split()))
ans=''
for i in range(len(p)):
    ans=ans+(chr(96+p[i]))
print(ans)
