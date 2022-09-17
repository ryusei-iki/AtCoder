
N=int(input())
wa=0
for i in range(N,0,-1):
    count=0
    for j in range(i,N+1,i):
        if(i%j==0):
            count=count+1
    wa=count*i+wa
print(wa)
'''
N = int(input())

ans = 0
D = [0] * (N+1)
for i in range(1, N+1):
    for j in range(i, N+1, i):
        D[j] += 1
    ans += i*D[i]
print(ans)
