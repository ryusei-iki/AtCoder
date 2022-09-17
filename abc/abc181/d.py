#整数 Counter


S=int(input())
SS=str(S)

lis=[0]*10
for i in range(len(SS)):
    lis[int(SS[i])]=lis[int(SS[i])]+1
con=0
if(len(SS)==2):
    if( ( (int(SS[0])*10+int(SS[1]) )%8==0 or (int(SS[1])*10+int(SS[0]))%8==0) ):
        print('Yes')
    else:
        print('No')
    exit()
    lis[0]=1
if(len(SS)==1):
    if(S%8==0):
        print('Yes')
    else:
        print('No')
    exit()
    lis[0]=2

for i in range(1,1000):
    if(i%2==0):
        a=int(i/2)
        aa=str(a)
        if(len(aa)<2):

            aaa=int(aa)
            if(aaa%4==0):
                li=[0]*10
                if(len(str(i))==2):
                    li[0]=1
                else:
                    li[0]=2
                for j in range(len(str(i))):
                    # print(aa[i])
                    li[int(str(i)[j])]=li[int(str(i)[j])]+1
                for j in range(len(li)):
                    # print(li[j],lis[j])
                    if(li[j]<=lis[j]):
                        con=con+1

                    else:
                        con=0
                        break
                if(con==10):
                    con=0
                    print('Yes')
                    exit()
        else:

            # print(a)
            # print(aa[-2],aa[-1])
            aaa=int(aa[-2])*10+int(aa[-1])

            if(aaa%4==0):
                li=[0]*10
                if(len(str(i))==2):
                    li[0]=1
                for j in range(len(str(i))):
                    # print(aa[i])
                    li[int(str(i)[j])]=li[int(str(i)[j])]+1
                for j in range(len(li)):
                    # print(li[j],lis[j])
                    if(li[j]<=lis[j]):
                        con=con+1

                    else:
                        con=0
                        break
                if(con==10):
                    con=0
                    print('Yes')
                    exit()


print('No')
