import math
N=int(input())
def num2alpha(num):
    if num<=26:
        return str.lower(chr(64+num))
    elif num%26==0:
        return str.lower(num2alpha(num//26-1)+chr(90))
    else:
        return str.lower(num2alpha(num//26)+chr(64+num%26))


print(num2alpha(N))
print(chr(64+N%26))
print(chr(90))
