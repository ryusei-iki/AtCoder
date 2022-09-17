N=int(input())
S=[0]*N
for i in range(N):
    S[i]=input()

a=[0]*4
for i in range(len(S)):
    if S[i]=='AC':
        a[0]=a[0]+1
    elif S[i]=='WA':
        a[1]=a[1]+1
    elif S[i]=='TLE':
        a[2]=a[2]+1
    elif( S[i]=='RE'):
        a[3]=a[3]+1

print('AC x {}'.format(a[0]))
print('WA x {}'.format(a[1]))
print('TLE x {}'.format(a[2]))
print('RE x {}'.format(a[3]))
