#全探索 set
#setは重複を減らすためではなく，検索がlog(n)にするために使っている
n=int(input())
s=[0]*n
for i in range(n):
    s[i]=input()



ss=set(s)

for i in ss:
    if('!'+i in ss):
        print(i)
        exit()
print('satisfiable')
