#全探索
n=int(input())
s=[0]*n
for i in range(n):
    s[i]=list(input())

for i in range(n):
    con=0
    for j in range(n):
        if(s[i][j]=='#'):
            if(j<6):
                con=con+1
            else:
                if(s[i][j-6]=='#'):
                    con=con
                else:
                    con=con+1
        elif(5<j):
            if(s[i][j-6]=='#'):
                con=con-1
            else:
                con=con
        if(con==4):
            print('Yes')
            exit()

for i in range(n):
    con=0
    for j in range(n):
        if(s[j][i]=='#'):
            if(j<6):
                con=con+1
            else:
                if(s[j-6][i]=='#'):
                    con=con
                else:
                    con=con+1
        elif(5<j):
            if(s[j-6][i]=='#'):
                con=con-1
            else:
                con=con
        if(con==4):
            print('Yes')
            exit()

for i in range(n-5):
    con=0
    for j in range(n-i):
        if(s[j+i][j]=='#'):
            if(j<6):
                con=con+1
            else:
                if(s[j+i-6][j-6]=='#'):
                    con=con
                else:
                    con=con+1
        elif(5<j):
            if(s[j+i-6][j-6]=='#'):
                con=con-1
            else:
                con=con
        if(con==4):
            print('Yes')
            exit()
for i in range(n-5):
    con=0
    for j in range(n-i):
        if(s[j][j+i]=='#'):
            if(j<6):
                con=con+1
            else:
                if(s[j-6][j+i-6]=='#'):
                    con=con
                else:
                    con=con+1
        elif(5<j):
            if(s[j-6][j+i-6]=='#'):
                con=con-1
            else:
                con=con
        if(con==4):
            print('Yes')
            exit()
for i in range(n-5):
    con=0
    for j in range(n-i):
        if(s[j+i][n-j-1]=='#'):
            if(j<6):
                con=con+1
            else:
                if(s[j+i-6][n-j-1+6]=='#'):
                    con=con
                else:
                    con=con+1
        elif(5<j):
            if(s[j+i-6][n-j-1+6]=='#'):
                con=con-1
            else:
                con=con
        if(con==4):
            print('Yes')
            exit()

for i in range(n-5):
    con=0
    for j in range(n-i):
        if(s[j][n-j-i-1]=='#'):
            if(j<6):
                con=con+1
            else:
                if(s[j-6][n-j-i-1+6]=='#'):
                    con=con
                else:
                    con=con+1
        elif(5<j):
            if(s[j-6][n-j-i-1+6]=='#'):
                con=con-1
            else:
                con=con
        if(con==4):
            print('Yes')
            exit()
print('No')
