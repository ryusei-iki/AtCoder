N=int(input())
X=input()
xx=int(X)
xxx=str(xx)
sa=N-len(xxx)
X_len=len(X)
a=0
for i in range(sa,N):
    a=int(X[i])*(2**(N-i-1))+a





fx=[-1]*(2*(10**5))
for i in range(X_len):
    ans=0
    if(X[i]=='0'):
        b=a+2**(X_len-i-1)
    else:
        b=a-2**(X_len-i-1)

    while(b!=0):

        fx=b%str(format(b,'b')).count('1')
        ans=ans+1
        b=fx

    print(ans)
