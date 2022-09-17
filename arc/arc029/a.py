N=int(input())
t=[0]*N
for i in range(N):
    t[i]=int(input())

min_takahashi=[0]*(1<<N)
min_tomodati=[0]*(1<<N)
min_all=[0]*(1<<N)
for i in range(1<<N):

    for j in range(N):
        if((i>>j) & 1==1):
            min_takahashi[i]=t[j]+min_takahashi[i]
        else:
            min_tomodati[i]=min_tomodati[i]+t[j]

    min_all[i]=max(min_takahashi[i],min_tomodati[i])


print(min(min_all))
