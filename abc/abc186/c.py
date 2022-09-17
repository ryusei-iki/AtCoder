#整数

N=int(input())




ans=0
for i in range(1,N+1):
    moji8=format(i,'o')

    if('7' not in moji8 and '7' not in str(i)):
        ans=ans+1


print(ans)
