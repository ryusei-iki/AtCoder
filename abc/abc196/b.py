
x=input()
ans=''
for i in range(len(x)):
    if(x[i]=='.'):
        print(ans)
        exit()
    else:
        ans=ans+x[i]
print(ans)
