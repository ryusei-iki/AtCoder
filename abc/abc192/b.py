#@
S=input()
for i in range(len(S)):

    if((i+1)%2==0):
        if(S[i].islower()):
            print('No')
            exit()
        else:
            pass
    else:
        if(S[i].islower()):
            pass
        else:
            print('No')
            exit()
print('Yes')
