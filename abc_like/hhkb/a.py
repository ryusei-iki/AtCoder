N=int(input())

p=list(map(int,input().split()))
print(p)

# p=list(set(p))

p.sort()
mi=p[0]
print(p)
if(p[0]!=p[1]):
    print(p[0])
    exit()
for i in range(len(p)+1,len(p)-1):
    if(p[i-1]!=p[i] and p[i]!=p[i+1]):
        print(p[i])
        exit()
if(p[len(p-1)] != p[-1]):
    print(p[-2])
