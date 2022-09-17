n=int(input())
ans=0
if(len(str(n))%2==1):
    print(int(10**((len(str(n))-1)/2)-1))
    exit()
else:

    for i in range(len(str(n))//2):
        if(str(n)[i]=='0'):
            pass
        elif(i==0):
            if(len(str(n))//2==(i+1)):
                tas=min(int(str(n)[i]),int(str(n)[-1]))
                ans=ans+tas
            else:
                ans=ans+int(str(n)[i])*int(10**(len(str(n))/2-i-1))-1
        else:
            if(len(str(n))//2==(i+1)):
                tas=min(int(str(n)[i]),int(str(n)[-1]))
                ans=ans+tas+1

            else:

                ans=ans+(int(str(n)[i])+1)*int(10**(len(str(n))/2-i-1))
        print(ans)

    # for i in range(len(str(n))):
    #     ans=ans+10**()
print(ans)
