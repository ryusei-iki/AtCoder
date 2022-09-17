#全探索
#三角形
n=int(input())
x=[0]*n
y=[0]*n
for i in range(n):
    x[i],y[i]=map(int,input().split())
ans=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if(x[i]==x[j] and x[j]==x[k]):
                continue
            else:
                if(y[i]==y[j] and y[j]==y[k]):
                    continue
                else:
                    ue_yoko=x[k]-x[j]
                    ue_tate=y[k]-y[j]
                    if(ue_yoko==0 or ue_tate==0):
                        ans=ans+1
                        continue
                    ue_kata=ue_tate/ue_yoko
                    sita_yoko=x[j]-x[i]
                    sita_tate=y[j]-y[i]
                    if(sita_yoko==0 or sita_tate==0):
                        ans=ans+1
                        continue
                    sita_kata=sita_tate/sita_yoko
                    if(ue_kata==sita_kata):
                        continue
                    else:
                        ans=ans+1
print(ans)
