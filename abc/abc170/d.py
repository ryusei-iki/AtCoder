
N=int(input())
A=[0]*N

A=list(map(int,input().split()))
A.sort(reverse)
warenai=[]
warenai.append(A[0])
for i in range(2*10**5):
    d=[j for j in range(B) if j%A[i]!=0]
    for j in range(2*10**5):
        if(A[j]%A[i]):

print(A)
