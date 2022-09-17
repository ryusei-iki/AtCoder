#全探索
#組合せ
#itertools

import itertools
s=[0]*3
for i in range(3):
    s[i]=input()


aru_check=[0]*26
s_aru=[0]*3
co=0
con=[0]*26
dame=set()
for i in range(3):
    s_aru[i]=[]
    for j in range(len(s[i])):

        if(aru_check[ord(s[i][j])-97]==0):
            con[ord(s[i][j])-97]=co
            co=co+1
        s_aru[i].append(con[ord(s[i][j])-97])
        aru_check[ord(s[i][j])-97]=1
        if(j==0):
            dame.add(con[ord(s[i][j])-97])

koko=0




if(11<=sum(aru_check)):
    print('UNSOLVABLE')
    exit()


seq=(0,1,2,3,4,5,6,7,8,9)
tamesu=list(itertools.permutations(seq,sum(aru_check)))




for i in range(len(tamesu)):
    ch=0
    for jj in range(len(list(dame))):
        # print(j)
        if(tamesu[i][list(dame)[jj]]==0):
            pass
        else:
            ch=ch+1
    if(ch==len(list(dame))):
        kekka=[0]*3
        for j in range(3):
            s_keisan=''
            for k in range(len(s_aru[j])):

                s_keisan=s_keisan+str(tamesu[i][s_aru[j][k]])

            kekka[j]=int(s_keisan)
        if(kekka[0]+kekka[1]==kekka[2]):
            for i in range(3):
                print(kekka[i])
            exit()
        else:
            pass
print('UNSOLVABLE')
