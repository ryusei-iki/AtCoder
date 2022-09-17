a=float(input())
if(0<=int(str(a)[-1]) and int(str(a)[-1])<=2):
    print(str(a)[:-2]+'-')
elif(3<=int(str(a)[-1]) and int(str(a)[-1])<=6):
    print(str(a)[:-2])

elif(7<=int(str(a)[-1]) and int(str(a)[-1])<=9):
    print(str(a)[:-2]+'+')
