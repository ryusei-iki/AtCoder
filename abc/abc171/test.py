import math
N=int(input())
a=int(math.log(N,26))

koremade=0
nokori=N
count=0
def num2alpha(num):
    if num<=26:
        return chr(64+num)
    elif num%26==0:
        return num2alpha(num//26-1)+chr(90)
    else:
        return num2alpha(num//26)+chr(64+num%26)


while(1):
    if(nokori-26**(count+1)==0):

        break
    elif(nokori-26**(count+1)<0):
        break
    else:
        nokori=nokori-26**(count+1)
        print(nokori)
    count=count+1
count=count+1
print(count)
print(nokori)

print(num2alpha(nokori))

'''

aru_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']
b=''
for i in range(count):

    if(i==count-1):

        b=b+aru_list[nokori%(26**(count-1))-1]
        print(b)
    else:
        print('sita')
        print(nokori//26**(count-i))
        b=b+aru_list[(nokori//(26)**(count-i)-1)]
        print(b)

print('answer')
print(b)
'''
def num2alpha(num):
    if num<=26:
        return chr(64+num)
    elif num%26==0:
        return num2alpha(num//26-1)+chr(90)
    else:
        return num2alpha(num//26)+chr(64+num%26)
