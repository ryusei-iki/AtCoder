#set
n=int(input())
l_a=[0]*n

for i in range(n):
    l_a[i]=list(map(int,input().split()))
check=[]
dame=0
ans=0

arr=list(map(list,set(map(tuple,l_a))))
print(len(arr))

# l_a=sorted(l_a)
# for i in range(n-1):
#     if(i in check):
#         pass
#     else:
#         for j in range(i+1,n):
#             if(l_a[i][0]==l_a[j][0]):
#                 for k in range(1,l_a[i][0]+1):
#                     if(l_a[i][k]==l_a[j][k]):
#                         pass
#                     else:
#                         dame=1
#                         break
#                 if(dame!=1):
#                     check.append(j)
#                     ans=ans+1
#                 dame=0
#             else:
#                 break
#
# print(n-ans)
