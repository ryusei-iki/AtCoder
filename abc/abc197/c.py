n=int(input())
a=list(map(int,input().split()))

mae=0
ans=0
hyouji=float('inf')
if(n==1):
    print(a[0])
    exit()
for i in range(1,2**n):
    # print(str(i)+'i')
    ans=0
    kekka=0
    mae=0
    for j in range(n-1):
        # print(str(j)+'j')
        kekka=0
        if((i>>j) &1):
            for k in range(j-mae+1):
                # print(n,k,mae)
                kekka=kekka | a[n-k-mae-1]
                # print(str(kekka)+'kekka')
                # print(ans)
            mae=j+1
            if(ans==0):
                # print('ue')
                ans=kekka
                # print(ans)
            else:
                # print('kita')
                ans=ans ^ kekka
    # print(ans)
    kekka=0
    for k in range(j-mae+2):
        # print(a[n-k-mae-1])
        kekka=kekka | a[n-k-mae-1]
        # print(str(kekka)+'kekka')
    if(ans==0):
        ans=kekka
    else:
        ans=ans ^ kekka
    # print(str(ans)+'saigo')
    hyouji=min(hyouji,ans)

print(hyouji)
