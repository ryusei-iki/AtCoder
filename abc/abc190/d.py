#整数
n=int(input())

sq=int((2*n)**0.5)
ans=0
for i in range(1,sq+1):

    if(2*n%i==0):
        if(i%2==(2*n/i)%2):
            pass
        else:
            ans=ans+1
print(ans*2)
