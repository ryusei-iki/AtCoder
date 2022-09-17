


N,W=map(int,input().split())
s=[0]*N
t=[0]*N
p=[0]*N
for i in range(N):
    s[i],t[i],p[i]=map(int,input().split())

doredake=[0]*(2*10**5+1)

for i in range(N):
    doredake[i]

for i in range(N):

    doredake[s[i]-1]=doredake[s[i]-1]+p[i]
    doredake[t[i]-1]=doredake[t[i]-1]-p[i]


for i in range(len(doredake)):
    doredake[i]=doredake[i]+doredake[i-1]
    if(W<doredake[i]):
        print('No')
        exit()

print('Yes')

# for i in doredake:
#     if(W<i):
#         print('No')
#         exit()
# print('Yes')
