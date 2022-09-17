N,K=map(int,input().split())
n_b=N
a=N%K
if(K/2<a):
    print(abs(a-K))
else:
    print(a)
