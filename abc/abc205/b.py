#全探索
n=int(input())
a=list(map(int,input().split()))
 
check=[0 for i in range(n)]
for i in a:
    check[i-1]=check[i-1]+1
    if(check[i-1]==2):
        print('No')
        exit()
print('Yes')