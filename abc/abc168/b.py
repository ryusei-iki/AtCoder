K=int(input())
S=input()

if(K>=int(len(S))):
    print(S)
else:
    a=S[0:K]

    print(a+'...')
