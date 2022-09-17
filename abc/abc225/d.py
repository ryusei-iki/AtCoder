#連結リスト
n,q=map(int,input().split())

mae=[-1 for i in range(n+1)]
usiro=[-1for i in range(n+1)]
for i in range(q):
    query=list(map(int,input().split()))
    if(query[0]==1):
        usiro[query[1]]=query[2]
        mae[query[2]]=query[1]
    elif(query[0]==2):
        usiro[query[1]]=-1
        mae[query[2]]=-1
    else:
        koko=query[1]

        while(mae[koko]!=-1):
            koko=mae[koko]
        ans_mae=[koko]
        while(usiro[koko]!=-1):
            ans_mae.append(usiro[koko])
            koko=usiro[koko]

        print(len(ans_mae),*ans_mae)
