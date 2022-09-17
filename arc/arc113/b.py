a,b,c=map(int,input().split())

a_first=str(a)[-1]


lis_1=[0,1,5,6]
lis_2=[4,9]
lis_4=[2,3,7,8]


lis_2_num=[0,0,0,0,6,0,0,0,0,1]

lis_3_num= [0,0,4,9,0,0,0,9,4]
lis_3_num1=[0,0,8,7,0,0,0,3,2]
lis_3_num2=[0,0,6,1,0,0,0,1,6]

lis_3=[]
if(int(a_first) in lis_1):
    print(a_first)
    exit()
elif(int(a_first) in lis_2):
    if(pow(b,c,2)==0):
        print(lis_2_num[int(a_first)])
    else:
        print(a_first)

    exit()
else:
    amari=pow(b,c,4)

    if(amari==0):
        print(lis_3_num2[int(a_first)])

    elif(amari==1):
        print(a_first)

    elif(amari==2):
        print(lis_3_num[int(a_first)])

    else:
        print(lis_3_num1[int(a_first)])
