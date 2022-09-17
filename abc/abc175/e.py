N,K=map(int,input().split())
P=list(map(int,input().split()))
C=list(map(int,input().split()))

def loop(tugi,con,i):
    if(tugi-1 in loop_check or K<=con):
        #print('b')
        return 0

    else:
        con=con+1
        #loop_check=
        #print('a')
        #print(tugi)
        loop_check.append(tugi-1)
        #print(C[tugi-1])
        #print(P[tugi-1])
        #'''
        #a=loop(P[tugi-1])
        loop_num_list[i].append(C[P[tugi-1]-1])
        return C[P[tugi-1]-1]+loop(P[tugi-1],con,i)
loop_num_list=[]
#print(loop_num_list)
loop_num=[]
loop_check=[]
for i in range(N):
    loop_num_list.append([])
    #print(loop_num_list)
    loop_num.append(loop(i+1,0,i))
    loop_check=[]
#print(loop_num)
#print()
#print(loop_num_list)
#print(max(loop_num))
print(loop_num_list)
print(loop_num)
b_max=-10**10
for i in range(len(loop_num_list)):
    c=-10**10
    cc=0
    if(0<loop_num[i]):
        a=K//len(loop_num_list[i])
        b=a*loop_num[i]
        for j in range(K%len(loop_num_list[i])):
            cc=cc+loop_num_list[i][j]
            c=max(c,cc)
        b=b+c
        b_max=max(b,b_max)
    else:
        for j in range(len(loop_num_list[i])):
            cc=cc+loop_num_list[i][j]
            c=max(c,cc)
        b_max=max(c,b_max)

print(b_max)
