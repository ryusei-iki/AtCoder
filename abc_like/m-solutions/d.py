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
    money=money+A[i]*kazu
    kazu=0
    if(A[i]<A[i+1]):
        kazu=money//A[i]
        money=money-A[i]*kazu

    elif(A[i+1]<=A[i]):
        pass

money=money+A[N-1]*kazu
print(money)
