n,m=map(int,input().split())
a=[0]*m
b=[0]*m
for i in range(m):
    a[i],b[i]=map(int,input().split())
lis=[[] for i in range(n)]
for i in range(m):
    lis[a[i]-1].append(b[i]-1)
    lis[b[i]-1].append(a[i]-1)
seen=[0]*n
ans=[0]*n


que=[0] #初期値は最初の探索の開始地点  forを回すことでqueに探索したところが追加される
dist=[None]*n #最初の探索の開始地点からの距離
cnt=[0]*n #添字の距離でどのくらいパターンが有るか
dist[0]=0#最初のところに行くためには移動しなくて良いため０
cnt[0]=1#最初のところに行くパターンは一個

for i in que:
    for j in lis[i]:
        if dist[j] is None:
            dist[j]=dist[i]+1
            que.append(j)
            cnt[j]=cnt[i]
        elif dist[j]==dist[i]+1:
            cnt[j]=(cnt[i]+cnt[j])%(10**9+7)
print(cnt[-1])