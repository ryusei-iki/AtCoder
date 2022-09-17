#全探索
a,b,c,d=map(int,input().split())
def han(num):
    if num <= 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False

        else:
            return True
kari=0
for i in range(a,b+1):
    kari=0
    for j in range(c,d+1):
        if(han(i+j)):
            pass
        else:
            kari=kari+1

    if(kari==d-c+1):
        print('Takahashi')
        exit()
print('Aoki')
