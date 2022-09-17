#@
a,b=map(int,input().split())
a=str(a)
b=str(b)
for i in range(min(len(a),len(b))):
    if(10<=int(a[-i-1])+int(b[-i-1])):
        print('Hard')
        exit()
print('Easy')
