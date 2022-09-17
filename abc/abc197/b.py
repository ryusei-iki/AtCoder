h,w,x,y=map(int,input().split())

s=[0]*h
for i in range(h):
    s[i]=input()
# print(s)
if(s[x-1][y-1]=='#'):
    print(0)
    exit()
ans=1
check_ue=0
check_sita=0
ue=0
sita=0
for i in range(1,h):
    # print(i)
    # print(str(ans)+'ans')
    if(x+i<=h and ue==0):
        if(s[x+i-1][y-1]=='.'):
            ans=ans+1
            # print('ki')
        else:
            ue=1
    else:
        check_ue=1

    if(0<x-i and sita==0):
        if(s[x-i-1][y-1]=='.'):
            ans=ans+1
        else:
            sita=1
    else:
        check_sita=1
    if(check_ue+check_sita==2):
        break
# print(ans)
check_ue=0
check_sita=0
ue=0
sita=0
for i in range(1,w):
    # print(i)
    if(y+i<=w and ue==0):
        if(s[x-1][y+i-1]=='.'):
            ans=ans+1
        else:
            ue=1
    else:
        check_ue=1

    if(0<y-i and sita==0):
        if(s[x-1][y-i-1]=='.'):
            ans=ans+1
        else:
            sita=1
    else:
        check_sita=1
    if(check_ue+check_sita==2):
        break
print(ans)
