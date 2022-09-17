#整数


N=int(input())

N_moji=str(N)
keta=len(N_moji)
wa=0


lis=[0]*10

for i in range(len(N_moji)):
    # print(N_moji[i])
    # print(lis[3])
    lis[int(N_moji[i])]=lis[int(N_moji[i])]+1
    wa=wa+int(N_moji[i])

# if(keta==1):
#     if(N%3==0):
#         print(0)
#         exit()
#     else:
#         print(-1)
#         exit()

if(wa%3==0):
    print(0)
    exit()
else:
    if(wa%3==2):
        if(0<lis[2] or 0<lis[5] or 0<lis[8]):
            print(1)
            exit()
        else:
            if(1<lis[1]+lis[4]+lis[7] and 2<keta):
                print(2)
                exit()
    else:
        if(0<lis[1] or 0<lis[4] or 0<lis[7]):
            print(1)
            exit()
        else:
            if(1<lis[2]+lis[5]+lis[8] and 2<keta):
                print(2)
                exit()
print(-1)
