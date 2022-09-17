#@
n=input()
n_len=len(str(n))
con_usiro=0
con_mae=0
for i in range(n_len):

    if(str(n)[i]=='0'):
        con_mae=con_mae+1
    else:
        break
for i in range(n_len):

    if(str(n)[-1*i-1]=='0'):
        con_usiro=con_usiro+1
    else:
        break

if(con_mae<con_usiro):

    henkei='0'*(con_usiro-con_mae)+str(n)
elif(con_usiro<con_mae):
    henkei=str(n)+'0'*(con_mae-con_usiro)
else:
    henkei=str(n)

for i in range(len(henkei)//2):

     if(henkei[i]==henkei[-1*i-1]):
        pass
     else:
        print('No')
        exit()
print('Yes')
