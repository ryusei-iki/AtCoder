#sort
n,k=map(int,input().split())
p=[0]*n
ima=[0]*n
for i in range(n):
    p[i]=list(map(int,input().split()))
    ima[i]=sum(p[i])

indices=[i for i in range(n)]
indices_sort=sorted(indices,key=lambda i: -ima[i])
ima_sort=[ima[i] for i in indices_sort]
jyun=[0 for i in range(n)]
mae=-1
mae_num=0
for i in range(n):
    if(mae==ima_sort[i]):
        jyun[indices_sort[i]]=jyun[indices_sort[i-1]]
    else:
        jyun[indices_sort[i]]=i+1
        mae=ima_sort[i]


# for i in range(n):
#     kari=ima[i]+300
#     for j in range(n):
#         if(ima_sort[j]<=kari):
#             if(jyun[indices_sort[j]]<=k):
#                 print('Yes')
#                 break
#         if(k<jyun[indices_sort[j]]):
#             print('No')
#             break

ans=[0]*n
mae=0
# print(ima)
# print(ima_sort)
# print(indices_sort)
# print(jyun)
# print('================')
dame=0
for i in range(n):
    kari=ima[indices_sort[i]]+300
    # print(kari)
    for j in range(mae,n):
        if(ima_sort[j]<=kari):
            if(jyun[indices_sort[j]]<=k):
                ans[indices_sort[i]]='Yes'
                mae=j
                break
            else:
                ans[indices_sort[i]]='No'
                dame=1
                break
        if(k<jyun[indices_sort[j]]):
            ans[indices_sort[i]]='No'
            dame=1
            break
    if(dame==1):
        break

for i in range(n):
    if(ans[i]==0):
        print('No')
    else:
        print(ans[i])
