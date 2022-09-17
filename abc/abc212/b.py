#@
x=input()
if(x[0]==x[1] and x[1]==x[2] and x[2]==x[3]):
    print('Weak')
    exit()
else:
    con=0
    for i in range(3):
        if(x[i]!='9'):

            if(int(x[i])+1==int(x[i+1])):
                con=con+1
        else:
            if(int(x[i+1])==0):
                con=con+1

    if(con==3):
        print('Weak')
        exit()

print('Strong')
