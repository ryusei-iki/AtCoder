s,k=map(str,input().split())
k=int(k)


# import itertools
# l=[0]*len(s)
# for i in range(len(s)):
#     l[i]=s[i]
# p_list = list(set(itertools.permutations(l, len(s))))
# p_list.sort()
# # print(p_list)
# print(*list(p_list[k-1]),sep='')
#
#
# def find(fl):
#     pass
#
#
# find(1<<len(s))
# print(1<<len(s))
p_list=set([])
lis=[0]*len(s)

print(lis)
def find(minn,maxx,depth,size):
    print(minn,maxx,depth,size)
    if(depth==size):
        p_list.add(tuple(lis))
        print(lis)
    else:
        for i in range(size-depth):

            lis[depth]=s[i+minn]
            find(minn+i+1,maxx,depth+1,size)
find(0,2,0,len(s))
print(p_list)
