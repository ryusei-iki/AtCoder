#全探索
N=int(input())
A=list(map(int,input().split()))
con_ans=0
ans=1
for j in range(2,1000+1):
    con=0
    for i in range(N):
        if(A[i]%j==0):
            con=con+1

    if(con_ans<con):
        con_ans=con
        ans=j



print(ans)
