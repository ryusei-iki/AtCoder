#@
#整数
n,k,a=map(int,input().split())
ans=[i for i in range(n)]
ans[0]=n

da=(k%n)
da=(da+a-1)%n

print(ans[da])
