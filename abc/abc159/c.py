L=int(input())
max=0
for i in range(L):
    for j in range(L-i):
        if(i*j*(L-i-j)>max):
            max=i*j*(L-i-j)
print(max)
