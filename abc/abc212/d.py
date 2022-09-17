#優先度付きキュー
#Priority Queue
import heapq
q=int(input())
p=[-1]*q
x=[-1]*q
for i in range(q):
    p[i]=list(map(int,input().split()))
    #p[i],x[i]=map(int,input().split())
s=0
que=[]
heapq.heapify(que)
for i in range(q):
    if(p[i][0]==1):
        heapq.heappush(que,p[i][1]-s)
    elif(p[i][0]==2):
        s=s+p[i][1]
    else:
        print(heapq.heappop(que)+s)
