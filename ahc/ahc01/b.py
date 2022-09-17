
n=int(input())
x=[0]*n
y=[0]*n
r=[0]*n
kibou=[0]*n
for i in range(n):
    kibou[i]=list(map(int,input().split()))

syutu=[0]*n

indices=[*range(n)]
sorted_indices=sorted(indices, key=lambda i: kibou[i][2])
sorted_num=[kibou[i] for i in sorted_indices]

for i in range(n):
    ima=sorted_num[sorted_indices[i]]
    syutu[i]=[ima[0],ima[1],ima[0]+1,ima[1]+1]
    print(*syutu[i])
