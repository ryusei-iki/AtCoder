#@
n=input()

if(int(n)<=999):
    print(0)
    exit()
ans=0
for i in range(1,len(n)+1):


    if(i*3+1==len(n)):

        ans=ans+i*(int(n[len(n)-(i+1)*3+2:len(n)])-10**(i*3)+1)
        break
    elif(i*3+2==len(n)):

        ans=ans+i*(int(n[len(n)-(i+1)*3+1:len(n)])-10**(i*3)+1)
        break
    else:
        if(i*3+3==len(n)):
            ans=ans+i*(int(n)-10**(i*3))+i
            break
        else:
            ans=ans+i*(10**((i+1)*3))-i*10**(i*3)

        #ans=ans+i*(10**(i+3)*3-10**(i*3))



print(ans)
