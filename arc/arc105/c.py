from collections import deque
N=int(input())
a=list(map(int,input().split()))


#
# # print(sum(a))
# print(42*15)
a.sort()
print(a)
for i in range(N-1):
    a[i+1]=a[i+1]/a[0]
print(a)

while(1):
    a=list(set(a))

    if(len(a)==1):
        print(a[0])
        exit()
    a.sort()
    # print(a)

    a.extend(([a[-1]-a[0]]))
    # print(a)
    a[-2]=a[0]
