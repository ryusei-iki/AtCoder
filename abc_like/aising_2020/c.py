N=int(input())
ans=[0]*(N)
hani=int(N**(0.5))+2
for i in range(1,hani):
    for j in range(1,hani):
        for k in range(1,hani):
            v=i**2+j**2+k**2+i*j+j*k+k*i
            if(v<=N):
                ans[v-1]=ans[v-1]+1
for i in ans:
    print(i)
