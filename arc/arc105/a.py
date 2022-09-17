


a=list(map(int,input().split()))
# if(a==b+c+d):
#     print('Yes')
# elif(a+b=c+d):
#     print('Yes')
# elif(a+b+c=d):
#     print('Yes')
# elif(a+b+d=c):
#     print('Yes')
# elif(a+c=b+d):
#     print('Yes')
# elif(a+c+d=b):
#     print('Yes')
# elif(a+d==b+c)
#     print('Yes')
# elif(a+d+c==b):
#     print('Yes')
# elif()

con=0


for i in range(2 ** 4):
    con=0
    for j in range(4):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            con=con+a[j]
    if(con==sum(a)/2):
        print('Yes')
        exit()


print('No')
