#式を勘違い

def nokori_min(muki,doko,r_min_num):
    noko_min=float('inf')
    noko_min_num=1

    if(muki==0):
        for i in range(n):
            if(i!=r_min_num):
                if(y[i]==doko):
                    if(r[i]<noko_min):
                        noko_min=r[i]
                        noko_min_num=i

    elif(muki==1):
            if(i!=r_min_num):
                if(x[i]==0):
                    if(r[i]<noko_min):
                        noko_min=r[i]
                        noko_min_num=i
    return noko_min_num

def syuturyoku(muki,doko,r_min_num,noko_min_num):
    syutu=[0]*n
    con=0
    #でかいスペースについて
     #向きがx方向
    if(muki==0):
        if(doko==0):
            syutu[r_min_num]=[0,1,10000,10000]
        elif(doko==9999):
            syutu[r_min_num]=[0,0,10000,9999]
    #向きがy方向
    elif(muki==1):
        if(doko==0):
            syutu[r_min_num]=[1,0,10000,10000]
        elif(doko==9999):
            syutu[r_min_num]=[0,0,9999,10000]


    #残りの一列or一行について
     #向きがx方向
    if(muki==0):
        if(doko==0):
            if(x[noko_min_num]<5000):
                syutu[noko_min_num]=[0,0,(10000-(n-2)),1]
                for i in range(n):
                    if(i!= r_min_num and i != noko_min_num):
                        syutu[i]=[(10000-(n-2))+con,0,(10000-(n-2))+1+con,1]
                        con=con+1
                    else:
                        pass
            else:
                syutu[noko_min_num]=[(n-2),0,10000,1]
                for i in range(n):
                    if(i!= r_min_num and i != noko_min_num):
                        syutu[i]=[0+con,0,0+con+1,1]
                        con=con+1
                    else:
                        pass
        elif(doko==9999):
            if(x[noko_min_num]<5000):
                syutu[noko_min_num]=[0,9999,(10000-(n-2)),10000]
                for i in range(n):
                    if(i!= r_min_num and i != noko_min_num):
                        syutu[i]=[(10000-(n-2))+con,9999,(10000-(n-2))+1+con,10000]
                        con=con+1
                    else:
                        pass
            else:
                syutu[noko_min_num]=[(n-2),9999,10000,10000]
                for i in range(n):
                    if(i!= r_min_num and i != noko_min_num):
                        syutu[i]=[0+con,9999,0+con+1,10000]
                        con=con+1
                    else:
                        pass

    #向きがy方向
    elif(muki==1):
        if(doko==0):
            if(y[noko_min_num]<5000):
                syutu[noko_min_num]=[0,0,1,(10000-(n-2))]
                for i in range(n):
                    if(i!= r_min_num and i != noko_min_num):
                        syutu[i]=[0,(10000-(n-2))+con,1,(10000-(n-2))+1+con]
                        con=con+1
                    else:
                        pass
            else:
                syutu[noko_min_num]=[0,(n-2),1,10000]
                for i in range(n):
                    if(i!= r_min_num and i != noko_min_num):
                        syutu[i]=[0,0+con,1,0+con+1]
                        con=con+1
                    else:
                        pass
        elif(doko==9999):
            if(y[noko_min_num]<5000):
                syutu[noko_min_num]=[9999,0,10000,(10000-(n-2))]
                for i in range(n):
                    if(i!= r_min_num and i != noko_min_num):
                        syutu[i]=[9999,(10000-(n-2))+con,10000,(10000-(n-2))+1+con]
                        con=con+1
                    else:
                        pass
            else:
                syutu[noko_min_num]=[9999,(n-2),10000,10000]
                for i in range(n):
                    if(i!= r_min_num and i != noko_min_num):
                        syutu[i]=[9999,0+con,10000,0+con+1]
                        con=con+1
                    else:
                        pass


    for i in range(n):
        print(*syutu[i])




n=int(input())
x=[0]*n
y=[0]*n
r=[0]*n
for i in range(n):
    x[i],y[i],r[i]=map(int,input().split())

# rの最小を探す rが小さければsを大きくし甲斐がある
r_min=float('inf')
for i in range(n):
    if(r[i]<r_min):
        r_min=r[i]
        r_min_num=i

#大きくしない広告をどこに置くかを決める


#まずはrが上か下か右か左の端にあるとき，
if(y[r_min_num]==9999 or y[r_min_num]==0 or x[r_min_num]==9999 or x[r_min_num]==0):
    if(y[r_min_num]==0 and x[r_min_num]==0):
        pass
    elif(y[r_min_num]==0 and x[r_min_num]==9999):
        pass
    elif(y[r_min_num]==9999 and x[r_min_num]==0):
        pass
    elif(y[r_min_num]==9999 and x[r_min_num==9999]):
        pass
    if(y[r_min_num]==0):
        muki=0
        doko=9999
        noko_min_num=nokori_min(muki,doko,r_min_num)
        syuturyoku(muki,doko,r_min_num,noko_min_num)

    elif(y[r_min_num]==9999):
        muki=0
        doko=0
        noko_min_num=nokori_min(muki,doko,r_min_num)
        syuturyoku(muki,doko,r_min_num,noko_min_num)

    elif(x[r_min_num]==0):
        muki=1
        doko=9999
        noko_min_num=nokori_min(muki,doko,r_min_num)
        syuturyoku(muki,doko,r_min_num,noko_min_num)

    elif(x[r_min_num]==9999):
        muki=1
        doko=0
        noko_min_num=nokori_min(muki,doko,r_min_num)
        syuturyoku(muki,doko,r_min_num,noko_min_num)


else:
    if(y[r_min_num]<5000):
        muki=0
        doko=9999
        noko_min_num=nokori_min(muki,doko,r_min_num)
        syuturyoku(muki,doko,r_min_num,noko_min_num)
    else:
        muki=0
        doko=0
        noko_min_num=nokori_min(muki,doko,r_min_num)
        syuturyoku(muki,doko,r_min_num,noko_min_num)
    print('-----------------')
