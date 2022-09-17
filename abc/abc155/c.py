N=int(input())
S=[0]*N
for i in range(N):
    S[i]=input()


dict={}
con=0
for i in S:
    if(i not in dict):
        dict[i]=1
    else:
        dict[i]=dict[i]+1

dic=sorted(dict.items(),key=lambda x:x[1],reverse=True)
ans=[]
for i in dic:
    mae=i[1]
    break
con=0
for i in dic:
    if(i[1]==mae):
        pass
    else:
        break
    ans.append(i[0])
    con=con+1

    mae=i[1]

ans.sort()

for i in ans:
    print(i)
