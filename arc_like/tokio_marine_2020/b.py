A,V=map(int,input().split())
B,W=map(int,input().split())

T=int(input())

sa=abs(A-B)
haya=V-W

if(sa<=0):
    print('NO')
elif(sa<=haya*T):
    print('YES')
    exit()
else:
    print('NO')
