#dict
#sort
x=input()
n=int(input())
s=[0]*n
for i in range(n):
    s[i]=input()

henkan={x[i]:chr(97+i) for i in range(len(x))}
gyaku={chr(97+i):x[i] for i in range(len(x))}

atai=[0]*n
kari=['' for i in range(n)]

for i in range(n):
    for j in range(len(s[i])):
        kari[i]=kari[i]+henkan[s[i][j]]

ato=sorted(kari)

ans=['' for i in range(n)]

for i in range(n):

    for j in range(len(ato[i])):
        ans[i]=ans[i]+gyaku[ato[i][j]]
for i in range(n):
    print(ans[i])
