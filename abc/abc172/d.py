

N=int(input())
'''
count=0
for i in range(1,N+1):
    n=N//i
    count=n*(i+i*n)//(2)+count
print(count)
'''
count=0
wa=0
for i in range(N,0,-1):

    count=0
    for j in range(1,N+1):
        if(i%j==0):
            count=count+1
    wa=count*i+wa
print(wa)
