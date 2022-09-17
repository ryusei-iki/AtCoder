N=int(input())
A=[0]*N
A=list(map(int,input().split()))
money=1000
money_temp=1000
kazu=0
ma=0
mi=float('inf')
stop=0
for i in range(0,N-1):
    if(A[i]<A[i+1]):
        money=money+kazu*ma
        ma=0
        mi=min(mi,A[i])
        #print('ue')
        #print(A[i])
        #print(A[i+1])
    elif(A[i]==A[i+1]):
        pass
    elif(A[i+1]<A[i]):
        stop=1
        ma=max(A[i],ma)

        kazu=money//mi
        money_temp=max(money_temp,money-mi*kazu)
        money=money-mi*kazu
        mi=float('inf')
        print(money)

money=money+kazu*A[N-1]

print(max(money,money_temp))
print(money)
