N=int(input())
count=0
for i in range(1,N+1):
    if(i%3==0 and i%5==0):
        a=1
    elif(i%3==0):
        a=1
    elif(i%5==0):
        a=1
    else:
        count=count+i
        
print(count)
