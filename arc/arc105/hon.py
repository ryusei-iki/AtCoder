N=int(input())
a=list(map(int,input().split()))



a.sort()

while(1):
    #print(a)
    con=0
    for i in range(len(a)-1):
        b=a[i+1]-a[i+1]//a[0]*a[0]
        if(b==0):
            a[i+1]=a[0]

        else:
            a[i+1]=a[i+1]-a[i+1]//a[0]*a[0]

    a=list(set(a))
    a.sort()
    if(len(a)==1):
        print(a[0])
        exit()

# print(a)
#
# while(1):
#     a=list(set(a))
#
#     if(len(a)==1):
#         print(a[0])
#         exit()
#     a.sort()
#     # print(a)
#
#     a.extend(([a[-1]-a[0]]))
#     # print(a)
#     a[-2]=a[0]
