#euler tour
#segment tree
import sys
input=sys.stdin.readline
sys.setrecursionlimit(2000000)
n,q=map(int,input().split())
x=list(map(int,input().split()))
edge=[[] for _ in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)

vk=[list(map(int,input().split())) for _ in range(q)]


euler_basyo=[]
euler_atai=[]
euler_basyo.append(1)
euler_atai.append(x[0])
check=[0]*(n+1)
check[1]=1

def dfs(koko):
    for i in range(len(edge[koko])):
        if(check[edge[koko][i]]==0):
            euler_basyo.append(edge[koko][i])
            euler_atai.append(x[edge[koko][i]-1])
            check[edge[koko][i]]=1
            dfs(edge[koko][i])
            euler_basyo.append(-edge[koko][i])
            euler_atai.append(-x[edge[koko][i]-1])
dfs(1)
euler_basyo.append(-1)
euler_atai.append(x[0])
euler_in=[0]*(n+1)
euler_out=[0]*(n+1)

for i in range(len(euler_basyo)):
    if(1<euler_basyo[i]):
        euler_in[euler_basyo[i]]=i
    else:
        euler_out[-euler_basyo[i]]=i


class SegTree2:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = [init_val[i],i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i]= self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])
    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = [x,k-self.num]

        while k > 1:
            #print(self.tree[k],self.tree[k^1])
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele
        l += self.num
        r += self.num
        koko=-1
        while l < r:
            if l & 1:
                res= self.segfunc(res,self.tree[l])
                l += 1
            if r & 1:
                res= self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

def segfunc2(x,y):
    if(x[0]<y[0]):
        return [y[0],y[1]]
    else:
        return [x[0],x[1]]
ide_ele = [-1,-1]


seg = SegTree2(euler_atai, segfunc2, ide_ele)
from collections import deque
hozon=deque()
for i in range(q):
    for j in range(vk[i][1]-1):
        da=seg.query(euler_in[vk[i][0]],euler_out[vk[i][0]])
        seg.update(da[1],-1)
        hozon.append(da)
    da=seg.query(euler_in[vk[i][0]],euler_out[vk[i][0]])
    print(da[0])
    seg.update(da[1],da[0])
    for i in range(vk[i][1]-1):
        kore=hozon.pop()
        seg.update(kore[1],kore[0])
