s=input()
mae=s[0:3]
ans=0
for i in range(len(s)-3):
    if(mae+s[i+3]=='ZONe'):
        ans=ans+1
    mae=s[i+1:i+4]
print(ans)
