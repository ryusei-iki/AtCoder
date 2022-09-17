N,K=map(int,input().split())
A=[0]
A=list(map(int,input().split()))
A.sort(reverse=True)
A_pura=[i for i in A if 0<=i]
A_mai=[-i for i in A if i<0]

print(A_pura)
print(A_mai)
A_pura.sort(reverse=True)
A_mai.sort(reverse=True)

seki=1
i_max=0
i_min=0
count=0
'''
for i in range(K):
    if(i==K-2):
        if(i_min%2==0):
            seki=seki*max(A_mai[i_min]*A_mai[i_min+1],A_pura[i_max]*A_pura[i_max+1])
        else:
            seki=seki*A_mai[i_min]*A_pura[i_max]
        print(seki%(10**9+7))
        break
    if(A_mai[i_min] < A_pura[i_max]):
        seki=seki*A_pure[i_max]
        i_max=i_max+1
    else:
        seki=seki*A_mai[i_min]
        i_min=i_min+1
'''

while(1):
    if(A_mai[i_min]*A_mai[i_min+1] < A_pura[i_max]*A_pura[i_max+1] or count+1==K):
        seki=seki*A_pura[i_max]
        i_max=i_max+1
        count=count+1
        if(count==K):
            print(seki)
            break
    else:
        seki=seki*A_mai[i_min]*A_mai[i_min+1]
        i_min=i_min+2
        count=count+2
        if(count==K):
            print(seki)
            break
