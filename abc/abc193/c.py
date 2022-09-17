#全探索
#set
#整数
n=int(input())
lis=set()
for i in range(2,int(n**(0.5)+1)):
    for j in range(2,n):
        if(n<i**j):
            break
        lis.add(i**j)
print(n-len(lis))
