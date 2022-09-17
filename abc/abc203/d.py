import math
n,k=map(int,input().split())
a=[0]*n
a_lis=[0]*(n*n)
con=0
for i in range(n):
    a[i]=list(map(int,input().split()))
    for j in range(len(a[i])):
        a_lis[con]=[a[i][j],i,j]
        con=con+1

print(a_lis)
a_lis.sort()
print(a_lis)
# print(math.floor(k**2/2))
# print(sorted(a[0:k][0:k]))
# kari=[]
# for i in range(k):
#     kari.extend(a[i][0:k])
# print(kari)
# saisyo=kari[math.floor(k**2/2)]
# print(saisyo)
# yoko=[0]*n
# for i in range(n):
#     yoko[i]=a[i][0:k]
# for i in yoko[0]:
#     if(i<saisyo):
#
# print(yoko)
# for i in range(n-k): #yoko
#     for j in range(n-k): #tate
#
#     print(yoko)
