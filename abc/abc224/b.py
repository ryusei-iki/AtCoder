#全探索
h,w=map(int,input().split())
a=[0]*h
for i in range(h):
    a[i]=list(map(int,input().split()))
for i in range(h-1):
    for j in range(i+1,h):
        for k in range(w-1):
            for l in range(k+1,w):
                if((a[i][k]+a[j][l])<=(a[j][k]+a[i][l])):
                    pass
                else:
                    print('No')
                    exit()
print('Yes')
