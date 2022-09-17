n,k=input().split()
a=n
k=int(k)
for i in range(k):
    a_lis=sorted(a)
    saidai=0
    saisyou=0
    for j in range(len(a)):
        saidai=saidai+int(a_lis[j])*10**(j)
    a_lis=sorted(a,reverse=True)
    for j in range(len(a)):
        saisyou=saisyou+int(a_lis[j])*10**(j)
    a=saidai-saisyou
    a=str(a)
print(a)
