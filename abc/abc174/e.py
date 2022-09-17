K=int(input())
nana=7
if(str(K)[-1]=='1'):
    while(1):
        #print(nana)
        if(nana%K==0):
            print(len(str(nana)))
            exit()

        nana=nana*10+7
elif(str(K)[-1]=='3'):
    while(1):
        #print(nana)
        if(nana%K==0):
            print(len(str(nana)))
            exit()

        nana=nana*10+7


elif(str(K)[-1]=='7'):
    while(1):
        #print(nana)
        if(nana%K==0):
            print(len(str(nana)))
            exit()

        nana=nana*10+7
print('-1')
