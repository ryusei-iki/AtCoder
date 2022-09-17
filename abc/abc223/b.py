#辞書順
#全探索
s=input()
iti=1
ni=len(s)
san=0
yon=1
saidai=s
saisyou=s
for i in range(len(s)-1):
    a=s[iti:ni]+s[san:yon]
    if(saidai<a):
        saidai=a
    if(a<saisyou):
        saisyou=a
    iti=iti+1
    ni=ni
    san=0
    yon=yon+1

print(saisyou)
print(saidai)
