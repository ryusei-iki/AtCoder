

N=int(input())

n=str(N)
n=n[-1]

if(n=='2' or n=='4' or n=='6' or n=='8'):
    if(n=='8'):
        a=0
    elif(n=='4'):
        a=1
    elif(n=='2'):
        a=2
    else:
        a=3
    #print(a)
else:
    print('-1')
    exit()

for i in range(1,N):
    if(N<5**i):
        break
    for j in range(0,N//4+2):

        if(5**i+3**(j*4+a+1)==N):
            print(j*4+a+1,i)
            exit()
        elif(N<5**i+3**(j*4+a)):
            break
print('-1')
