#全探索 0除算
N=int(input())
x=[0]*N
y=[0]*N
for i in range(N):
    x[i],y[i]=map(int,input().split())
#
# for i in range(N-2):
#     for j in range(i+1,N-1):
#         for k in range(j+1,N):
#             xx=x[j]-x[i]
#             yy=y[j]-y[i]
#             xxx=x[k]-x[j]
#             yyy=y[k]-y[j]
#             if(xx==0 or xxx==0 or yy==0 or yyy==0):
#                 if(xx==0 and xxx==0):
#
#                     print('Yes')
#                     exit()
#                 elif(yy==0 and yyy==0):
#
#                     print('Yes')
#                     exit()
#             else:
#
#                 kata=yy/xx
#                 if(0<kata):
#                     if(x[i]<x[j] and x[i]<x[j]):
#
#                         if(x[j]<x[k] and y[j]<y[k]):
#                             katakata=yyy/xxx
#                             if(abs((kata))==abs( (katakata))):
#                             # print('a')
#                             # print(i,j,k)
#                                 print('Yes')
#                                 exit()
#
#
#                         elif(x[i]<x[k]<x[j] and y[i]<y[k]<y[j]):
#                             katakata= (yyy)/ (xxx)
#                             if(abs( (kata))==abs( (katakata))):                        # print('a')
#                             # print(i,j,k)
#                                 print('Yes')
#                                 exit()
#                         elif(x[k]<x[i] and y[k]<y[i]):
#                             katakata= (yyy)/ (xxx)
#                             if(abs( (kata))==abs( (katakata))):                        # print('a')
#                             # print(i,j,k)
#                                 print('Yes')
#                                 exit()
#                     else:
#                         if(x[i]<x[k] and y[i]<y[k]):
#                             katakata= (yyy)/ (xxx)
#                             if(abs( (kata))==abs( (katakata))):
#                             # print('a')
#                             # print(i,j,k)
#                                 print('Yes')
#                                 exit()
#
#                         elif(x[j]<x[k]<x[i] and y[j]<y[k]<y[i]):
#                             katakata= (yyy)/ (xxx)
#                             if(abs( (kata))==abs( (katakata))):                        # print('a')
#                             # print(i,j,k)
#                                 print('Yes')
#                                 exit()
#                         elif(x[k]<x[j] and y[k]<y[j]):
#                             katakata= (yyy)/ (xxx)
#                             if(abs( (kata))==abs( (katakata))):                        # print('a')
#                             # print(i,j,k)
#                                 print('Yes')
#                                 exit()
#
#
#                 else:
#                     if(x[i]<x[j] and y[j]<y[i]):
#
#                         if(x[k]<x[i] and y[i]<y[k]):
#                             katakata= (yyy)/ (xxx)
#                             if(abs( (kata))==abs( (katakata))):                        # print('a')
#                             # print(i,j,k)
#                                 print('Yes')
#                                 exit()
#                         elif(x[i]<x[k]<x[j] and y[j]<y[k]<y[i]):
#                             katakata= (yyy)/ (xxx)
#                             if(abs( (kata))==abs( (katakata))):                        # print('a')
#                             # print(i,j,k)
#                                 print('Yes')
#                                 exit()
#                         elif(x[j]<x[k] and y[k]<y[j]):
#                             katakata= (yyy)/ (xxx)
#                             if(abs( (kata))==abs( (katakata))):                        # print('a')
#                             # print(i,j,k)
#                                 print('Yes')
#                                 exit()
#                     else:
#                         if(x[k]<x[j] and y[j]<y[k]):
#                             katakata= (yyy)/ (xxx)
#                             if(abs( (kata))==abs( (katakata))):                        # print('a')
#                             # print(i,j,k)
#                                 print('Yes')
#                                 exit()
#                         elif(x[j]<x[k]<x[i] and y[i]<y[k]<y[j]):
#                             katakata= (yyy)/ (xxx)
#                             if(abs( (kata))==abs( (katakata))):                        # print('a')
#                             # print(i,j,k)
#                                 print('Yes')
#                                 exit()
#                         elif(x[i]<x[k] and y[k]<y[i]):
#                             katakata= (yyy)/ (xxx)
#                             if(abs( (kata))==abs( (katakata))):                        # print('a')
#                             # print(i,j,k)
#                                 print('Yes')
#                                 exit()
#
#
# print('No')
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if((y[j]-y[i])*(x[k]-x[i])==(y[k]-y[i])*(x[j]-x[i])):
                print('Yes')
                exit()

print('No')
