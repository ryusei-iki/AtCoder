import collections
s = collections.deque(list(input()))
q = int(input())
rev = 0
for i in range(q):
    tfc = list(input().split())
    if tfc[0]=='1':
        rev = abs(rev-1)
    else:
        t,f,c = tfc
        print('{},{},{}'.format(t,f,c))
        if rev:
            if f=='1':
                s.append(c)
            else:
                s.appendleft(c)
        else:
            if f=='1':
                s.appendleft(c)
            else:
                s.append(c)
if rev:
    t = []
    for i in range(len(s)):
        t.append(s.pop())
    print(''.join(t))
else:
    print(''.join(s))
