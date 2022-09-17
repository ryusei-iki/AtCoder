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
    syutu[sorted_indices[i]]=[sorted_num[i][0],sorted_num[i][1],sorted_num[i][0]+1,sorted_num[i][1]+1]

print('----------------------')
for i in range(n):
    print(*syutu[i])
con=0
for i in range(n):

    ima_i=sorted_num[sorted_indices[i]]
    dame=sorted_indices[i]

    x_min_l=float('inf')
    x_min_r=float('inf')
    y_min_l=float('inf')
    y_min_r=float('inf')
    for j in range(n):
        print(ima_i)
        print(syutu[sorted_indices[j]])
        if(==j):
            pass
        else:


            ima_j=syutu[sorted_indices[j]]
            if(ima_j[0]<ima_i[0]):
                x_min_l=min(x_min_l,ima_i[0]-ima_j[0])

            elif(ima_j[0]==ima_i[0]):
                x_min_l=0
                x_min_r=0
            else:
                # print(x_min_r)
                # print(ima_j[0])
                # print(ima_i[0])
                x_min_r=min(x_min_r,ima_j[0]-ima_i[0])

            if(ima_j[1]<ima_i[1]):
                y_min_l=min(y_min_l,ima_i[1]-ima_j[1])

            elif(ima_j[1]==ima_i[1]):
                y_min_l=0
                y_min_r=0
            else:
                y_min_r=min(y_min_r,ima_j[1]-ima_i[1])
            # print(j)
            # print(syutu[j])
            # print(x_min_l,x_min_r,y_min_l,y_min_r)
            input()

    print(x_min_l,x_min_r,y_min_l,y_min_r)
    syutu[i]=[ima_i[0]-x_min_l,ima_i[1]-y_min_l,ima_i[0]+x_min_r,ima_i[1]+y_min_r]

for i in range(n):
    print(*syutu[i])
