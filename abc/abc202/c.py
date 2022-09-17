#全探索
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))


a_check=[[]for i in range(n)]
b_check=[[]for i in range(n)]
c_check=[[]for i in range(n)]

for i in range(n):
    a_check[a[i]-1].append(i+1)
    b_check[b[i]-1].append(i+1)
    c_check[c[i]-1].append(i+1)

ans=0
# for i in range(n):
#     for j in (b_check[a[i]-1]):
#         ans=ans+len(c_check[j-1])
# print(ans)
#
# for i in range(n):
#     b_check[c[i]-1]=b_check[c[i]-1]+1
# for i in range(n):
#     a_check[b[i]]=
# print(a_check)
# print(b_check)
# print(c_check)
for i in range(n):
    ans=ans+len(c_check[i])*(len(a_check[b[i]-1]))
print(ans)
