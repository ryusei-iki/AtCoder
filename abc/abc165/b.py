X=int(input())


a=100

count=0
while(1):
    count=count+1
    a=int(a*0.01+a)

    if(a>=X):
        print(count)
        break
