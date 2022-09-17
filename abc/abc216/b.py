
n=int(input())
s=[0]*n
t=[0]*n
for i in range(n):
    s[i],t[i]=map(str,input().split())

for i in range(n-1):
    for j in range(i+1,n):
        if(s[i]==s[j] and t[i]==t[j]):
            print('Yes')
            exit()
print('No')
