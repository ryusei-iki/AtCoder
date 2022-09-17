import math
N=int(input())
a=int(math.log(N,26))

def saiki(nokori):
    if(nokori<26):

        return aru_list[nokori]
    else:
        return saiki(nokori//26)+aru_list[nokori%26]

koremade=0
nokori=N
count=0

while(1):
    if(nokori-26**(count+1)==0):

        break
    elif(nokori-26**(count+1)<0):
        break
    else:
        nokori=nokori-26**(count+1)

    count=count+1
count=count+1


nokori=nokori-1

aru_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b=''
ans=saiki(nokori)


while(1):
    if(len(ans)==count):
        print(ans)
        exit()
    else:
        ans='a'+ans
