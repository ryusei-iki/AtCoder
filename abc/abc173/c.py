import copy
H,W,K=map(int,input().split())
CC=[0]*H
for i in range(H):
    CC[i]=list(input())

count=0
shar=0
kurokuro=0
for i in range(H):
    kurokuro=CC[i].count('#')+kurokuro


#print(kurokuro)
ans=0
for i in range(2**(H+W)):
    kuro=kurokuro
    c=copy.deepcopy(CC)

    for j in range(H+W):
        if((i>>j) & 1):
            if(j<H):
                for q in range(W):
                    if(c[j][q]=='#'):
                        shar=shar+1
                        c[j][q]='.'
                kuro=kuro-shar

                shar=0
            else:
                for q in range(H):
                    if(c[q][j-H]=='#'):
                        shar=shar+1
                        c[q][j-H]='.'

                kuro=kuro-shar
                shar=0

    if(kuro==K):
        ans=ans+1
print(ans)
