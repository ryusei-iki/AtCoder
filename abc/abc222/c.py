n,m=map(int,input().split())
a=[0 for i in range(2*n)]
for i in range(2*n):
    a[i]=input()


def kekka(iti,ni):
    if(iti=='G' and ni=='C'):
        return 1
    elif(iti=='G' and ni=='P'):
        return 2
    elif(iti=='G' and ni=='G'):
        return 3
    elif(iti=='C' and ni=='C'):
        return 3
    elif(iti=='C' and ni=='P'):
        return 1
    elif(iti=='C' and ni=='G'):
        return 2
    elif(iti=='P' and ni=='C'):
        return 2
    elif(iti=='P' and ni=='P'):
        return 3
    elif(iti=='P' and ni=='G'):
        return 1
ans=[0 for i in range(2*n)]
indices=[i for i in range(n*2)]
sorted_indices=sorted(indices,key=lambda i :-ans[i])
for i in range(m):
    for j in range(n):
        iti=a[sorted_indices[j*2]][i]
        ni=a[sorted_indices[j*2+1]][i]
        kotae=kekka(iti,ni)
        if(kotae==1):
            ans[sorted_indices[j*2]]=ans[sorted_indices[j*2]]+1
        elif(kotae==2):
            ans[sorted_indices[j*2+1]]=ans[sorted_indices[j*2+1]]+1
        else:
            pass

    sorted_indices=sorted(indices,key=lambda i :-ans[i])
for i in range(2*n):
    print(sorted_indices[i]+1)
