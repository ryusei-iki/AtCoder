def binary_search_lower(goal,start,owari):

    if(start==owari):
        return start
    
    elif(c[(owari+start)//2]<goal):
        #print(goal,(owari+start)//2,owari)
        basyo=binary_search_lower(goal,(owari+start)//2+1,owari)
    elif(goal<=c[(owari+start)//2]):

        basyo=binary_search_lower(goal,start,(owari+start)//2)

    return basyo

c=[]#探索対象
c=[1,2,3,5,5,5,6,7]
goal=5 #見つけたい数字
start=0
owari=len(c)
basyo=binary_search_lower(goal,start,owari)
print(basyo)