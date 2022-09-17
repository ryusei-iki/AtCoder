N,S=map(str,input().split())
N=int(N)

a=[[0 for i in range(N)] for j in range(N)]
print(a)

for i in range(N):
    for j in range(i,N):
        print(a)
        if(i==j):
            a[i][j]=S[i]
        else:
            a[i][j]=a[i][j-1]+S[j]


print(a)
ans=0
for i in a:
    for j in reversed(i):
        if(j==0):
            break
        for k in len(j):
            if(j[k]==j[len(j)-k]):
                if()

            else:
                break
#         if(j==0):
#             break
#
#
#         if(j==''.join(list(reversed(j))) and len(j)!=1):
#             print(j)
#             print(''.join(list(reversed(j))))
#             ans=ans+1
# print(ans)
