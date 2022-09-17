N,K=map(int,input().split())
p=[]
p=list(map(int,input().split()))

p.sort()
print(sum(p[0:K]))
