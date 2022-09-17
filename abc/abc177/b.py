#全探索
S=list(input())
T=list(input())
#print(S)
#print(T)
con=[0]*len(S)
for i in range(len(S)-len(T)+1):
    #print(i)
    for j in range(len(T)):
        if(S[i+j]==T[j]):
            con[i]=con[i]+1
print(len(T)-max(con))
