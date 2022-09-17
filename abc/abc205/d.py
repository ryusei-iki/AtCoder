#binary search
import sys
 
sys.setrecursionlimit(2000000)
n,q=map(int,input().split())
a=list(map(int,input().split()))
a.insert(0,0)
k=[0]*q
for i in range(q):
    k[i]=int(input())
c=[0]*(n+1)
for i in range(n):
    c[i+1]=a[i+1]-(i+1)
def usiro(goal,basyo):
    if(basyo==0):
        return basyo
    if(goal==c[basyo-1]):
        basyo=usiro(goal,basyo-1)
    return basyo
def nibun(goal,start,owari):

    if(start==owari):
        return start
    
    elif(c[(owari+start)//2]<goal):
        #print(goal,(owari+start)//2,owari)
        basyo=nibun(goal,(owari+start)//2+1,owari)
    elif(goal<=c[(owari+start)//2]):

        basyo=nibun(goal,start,(owari+start)//2)

    return basyo
 


for i in range(q):

 
    if(c[-1]<k[i]):
        print(a[-1]+k[i]-c[-1])
        
    else:

        koko=nibun(k[i],0,n)
        print(a[koko]-1-c[koko]+k[i])
