def prime():
    x=int(input())
    prime_count=x-2
    for i in range(2,int(x**(0.5))+1):
        for j in range(2,i):
            if(i%j==0):
                prime_count-=1
                break
    print(prime_count)
prime()
