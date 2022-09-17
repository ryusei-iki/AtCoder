#@
a,b=map(int,input().split())

if(int(str(a)[0])+int(str(a)[1])+int(str(a)[2])<int(str(b)[0])+int(str(b)[1])+int(str(b)[2])):
    print(int(str(b)[0])+int(str(b)[1])+int(str(b)[2]))
elif(int(str(a)[0])+int(str(a)[1])+int(str(a)[2])>int(str(b)[0])+int(str(b)[1])+int(str(b)[2])):
    print(int(str(a)[0])+int(str(a)[1])+int(str(a)[2]))
else:
    print(int(str(a)[0])+int(str(a)[1])+int(str(a)[2]))
