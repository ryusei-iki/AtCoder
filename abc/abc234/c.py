#整数
k=int(input())
ans=''
bin_str=format(k,'b')
for i in range(len(bin_str)):
    if(bin_str[i]=='1'):
        ans=ans+'2'
    else:
        ans=ans+'0'
print(ans)
