#全探索

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

b_max=0
a_max=a[0]

kari_3=0
for i in range(n):

    a_max=max(a_max,a[i])
    kari_2=a_max*b[i]
    kari_3=max(kari_2,kari_3)
    print(kari_3)
