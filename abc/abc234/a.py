#@
a=int(input())
def kan(a):
    return a**2+2*a+3

print(kan(kan(kan(a)+a)+kan(kan(a))))
