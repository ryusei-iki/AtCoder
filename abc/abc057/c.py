N=int(input())

for i in range(1,N+1):
    if(N%i==0):
        j=int(N/i)
        ans=max(len(str(i)),len(str(j)))

    if(N<i**2):
        break
print(ans)
