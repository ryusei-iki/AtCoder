n,k=map(int,input().split())
a=[]
ab=[]
b=[]
for i in range(n):
    ab.append(list(map(int,input().split())))

ab.sort()

ima=0
con=0
while(1):
    if(k<ab[con][0]-ima):
        print(ima+k)
        break
    else:
        k=k+ab[con][1]-(ab[con][0]-ima)
        ima=ab[con][0]
        con=con+1
        if(con==n):
            print(min(ima+k,10**100))
            break
        if(ima==10**100):
            print(10**100)
            break
