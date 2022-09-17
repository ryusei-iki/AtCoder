T=input()




T_hoge=[]

for i in range(len(T)):
    if '?' == T[i]:
        T_hoge.append('D')
    else:
        T_hoge.append(T[i])

A=''.join(T_hoge)
print(A)
