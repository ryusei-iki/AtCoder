a,b=map(int,input().split())
aa=format(a,'08b')
bb=format(b,'08b')

ans=''
for i in range(8):
    if(bb[i]=='0'):
        ans=ans+aa[i]
    else:
        ans=ans+str(-int(aa[i])+1)

print(int(ans,2))
