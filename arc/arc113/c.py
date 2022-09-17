s=input()

arufa=[chr(i) for i in range(97,97+26)]

d={i : 0 for i in arufa}


print(d)
mae=None
mae_num=0
hatu=1
tigau=0
ans=0
mae_blo=None
for i in range(len(s)):
    print(mae,s[i])
    if(mae==s[i]):
        if(d[s[i]]==0 and hatu!=0):
            hatu=1
            ans=ans-tigau
            mae==s[i]
            mae_blo=s[i]
        else:
            mae=s[i]
            pass
    else:
        if(hatu==0):
            hatu=0
            ans=ans+len(s)-(i+1)+1
            mae_num=i+1
            tigau=1
        else:
            if(mae_blo!=s[i] and mae_blo!=None):
                tigau=tigau+1
            else:
                mae=s[i]
print(ans)
