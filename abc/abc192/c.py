#全探索
n,k=map(int,input().split())

a=n
num=[-1]*11
max=0
min=0
for i in range(k):

    aa=str(a)
    # print(len(aa))

    for i in range(11):
        if(len(aa)-1<i):
            if(num[i-1]!=float('inf')):
                num[i]=float('inf')
            num[i]=-1
        else:
            # print(aa[i])
            num[i]=int(aa[i])

    save=i
    # print(num)
    num.sort()
    # print(num)
    count=0
    max=0
    for i in range(len(num)):
        if(num[i]==float('inf')):
            # print('ue')
            break
        if(num[i]==-1):
            count=count+1
        else:
            max=max+num[i]*10**(i-count)
    # print(max)
    # print('---------------')
    num.sort(reverse=True)
    #
    # print(num)
    min=0
    for i in range(len(num)):
        if(num[i]==-1):
            # print('sita')
            break
        min=min+num[i]*10**(i)
    #     print(min)
    # print(min)
    a=max-min
    # print(a)
print(a)
