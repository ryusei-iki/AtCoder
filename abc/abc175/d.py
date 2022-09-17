N,K=map(int,input().split())
P=list(map(int,input().split()))
C=list(map(int,input().split()))

def loop(tugi):
    if(tugi-1 in loop_check):
        print('b')
        return 0

    else:

        #loop_check=
        print('a')
        print(tugi)
        loop_check.append(tugi-1)
        #print(C[tugi-1])
        #print(P[tugi-1])
        #'''
        #a=loop(P[tugi-1])
        return max(C[tugi-1]+loop(P[tugi-1]),C[tugi-1])
loop_num=[]
loop_check=[]
for i in range(N):
    loop_num.append(loop(P[i]))
    loop_check=[]
print(loop_num)
print(max(loop_num))
