import math

def combinations_count(n, r):
    #print(math.factorial(n) // (math.factorial(n - r) * math.factorial(r)))
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


N=int(input())
a=[int(i) for i in input().split()]

c=[0 for i in range(N+1)]
g=[0 for i in range(N+1)]
l = [3, 3, 2, 1, 5, 1, 4, 2, 3]

print(set(l))
# {1, 2, 3, 4, 5}

print(list(set(l)))
# [1, 2, 3, 4, 5]
aa=str(a)
print(aa)
ran=set(aa)
print(ran)
wa=0
for i in range(list(set(aa))):
    #b[a[i]-1]=b[a[i]-1]+1

    g[i]=str(a).count(str(i))
    #print(g[i])
    #print(str(a))
    #print(i)
    if(g[i]>1):
        c[i]=(g[i]*g[i]-1)/2
        wa=c[i]+wa
    #    print(g)
    #    print(c[i])
    else:
        c[i]=0

        #print(c[i])


wawa=wa
#print(wa)
for i in range(1,N+1):

    wa=wa-g[a[i-1]]+1
    #print(g[a[i]-1])
    print(wa)
    wa=wawa
