#オーダー
n=int(input())
a=list(map(int,input().split()))

a=a[:min(8,n)]
# print(a,len(a))
lis=[0]*200
for i in range(1,2**len(a)):
    wa=0
    for j in range(len(a)):
        if((i>>j)&1):
            wa=wa+a[j]
            wa=wa%200

    lis[wa]=lis[wa]+1

for i in range(len(lis)):
    if(2<=lis[i]):
        dore=i
        break
else:
    print('No')
    exit()
b=[]
c=[]
# print(len(b))
# print('--------')
for i in range(1,2**len(a)):
    ans=[]
    wa=0
    for j in range(len(a)):
        # if((i>>j)&1):
        if(i&(1<<j)):
            # wa=(wa+a[j]%200)%200
            wa=wa+a[j]
            wa=wa%200
            ans.append(j+1)
    if(wa==dore and len(b)==0):
        b=ans
    elif(wa==dore):
        c=ans
        break
print('Yes')
print(len(b),*b)
print(len(c),*c)
# a=a[:min(8,n)]
# for i in range()
