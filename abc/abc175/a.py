S=input()
a=1
count=0
for i in range(len(S)):
    if(S[i]=='R') :
        if(count==0):
            a=1
            count=count+1
        elif(S[i-1]=='R'):
            count=count+1

print(count)
