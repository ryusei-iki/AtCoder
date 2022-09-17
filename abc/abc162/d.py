N=int(input())
S=input()
count=0
count=S.count('R')*S.count('G')*S.count('B')
for i in range(N-2):
    for j in range(1,(N+i+1)//2-i):

        if(S[i]+S[i+j]+S[i+2*j] in ['RGB','RBG','GRB','GBR','BGR','BRG']):

            count=count-1
print(count)
