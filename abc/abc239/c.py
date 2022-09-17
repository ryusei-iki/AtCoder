#全探索
x1,y1,x2,y2=map(int,input().split())

ans1=[]
ans2=[]
for i in range(6):
    for j in range(6):
        if((x1-(x1-i))**2+(y1-(y1-j))**2==5):
            ans1.append([x1-i,y1-j])
        if((x1-(x1+i))**2+(y1-(y1+j))**2==5):
            ans1.append([(x1+i),(y1+j)])
        if((x1-(x1+i))**2+(y1-(y1-j))**2==5):
            ans1.append([(x1+i),(y1-j)])
        if((x1-(x1-i))**2+(y1-(y1+j))**2==5):
            ans1.append([(x1-i),(y1+j)])

for i in range(6):
    for j in range(6):
        if((x2-(x2-i))**2+(y2-(y2-j))**2==5):
            ans2.append([x2-i,y2-j])
        if((x2-(x2+i))**2+(y2-(y2+j))**2==5):
            ans2.append([(x2+i),(y2+j)])
        if((x2-(x2-i))**2+(y2-(y2+j))**2==5):
            ans2.append([x2-i,y2+j])
        if((x2-(x2+i))**2+(y2-(y2-j))**2==5):
            ans2.append([(x2+i),(y2-j)])
# print(ans1)
# print(ans2)
for i in range(len(ans1)):
    for j in range(len(ans2)):
        if(ans1[i]==ans2[j]):
            print('Yes')
            exit()
print('No')
# a=set(tuple(ans1))
# if(len(ans1)==len(list(set(ans1)))):
#     print('No')
# else:
#     print('Yes')
