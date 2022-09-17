
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
print('-----------------------------')
for i in range(n):
    ima=sorted_num[sorted_indices[i]]
    syutu[i]=[ima[0],ima[1],ima[0]+1,ima[1]+1]


con=0
for i in range(n):

    ima_i=sorted_num[sorted_indices[i]]
    meyasu=int(ima_i[2]**(0.5))
    print('meyasu')
    print(meyasu)
    for j in range(n):
        if(i==j):
            pass
        else:
            ima_j=syutu[sorted_indices[j]]

            if(ima_j[0]<ima_i[0]):
                x_min_l=min(x_min_l,ima_i[0]-ima_j[0])

            elif(ima_j[0]==ima_i[0]):
                x_min_l=0
                x_min_r=0
            else:
                x_min_r=min(x_min_r,ima_j[0]-ima_i[0])

            if(ima_j[1]<ima_i[1]):
                y_min_l=min(y_min_l,ima_i[1]-ima_j[1])

            elif(ima_j[1]==ima_i[1]):
                y_min_l=0
                y_min_r=0
            else:
                y_min_r=min(y_min_r,ima_j[1]-ima_i[1])

            x_min=min(x_min,)
            if((ima_j[0])<(ima_i[0]-meyasu) and (ima_i[1]-meyasu)<(ima_j[1]) and (ima_j[2])<(ima_i[0]+meyasu+1) and (ima_i[1]+meyasu+1)<(ima_j[3])):
                con=con+1
            else:
                break
    print(con)
    if(con==n):
        syutu=[ima_i[0]-meyasu,ima_i[1]-meyasu,ima_i[0]+meyasu+1,ima[1]+meyasu+1]
    else:
        pass
    con=0

for i in range(n):
    print(*syutu[i])
