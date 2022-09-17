#@
s=input()
t=input()
s=list(s)
t=list(t)
tigau=[]
for i in range(len(s)):
    if(s[i]!=t[i]):
        tigau.append(i)
    else:
        pass
if(len(tigau)==0):
    print('Yes')
elif(len(tigau)==2):
    if(tigau[0]+1==tigau[1]):
        temp=s[tigau[1]]
        s[tigau[1]]=s[tigau[0]]
        s[tigau[0]]=temp
        if(s==t):
            print('Yes')
        else:
            print('No')
    else:
        print('No')
else:
    print('No')

