from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [0 for _ in range(M)]
    B = [0 for _ in range(M)]
    union = UnionFind(N)
    for i in range(M):
        A[i], B[i] = map(int, input().split())
        if union.same(A[i] - 1, B[i] - 1):
            print('No')
            exit()
        union.union(A[i] - 1, B[i] - 1)
    dic = dict()
    for i in range(M):
        if A[i] in dic.keys():
            if dic[A[i]] == 2:
                print('No')
                exit()
            dic[A[i]] = dic[A[i]] + 1
        else:
            dic[A[i]] = 1
        if B[i] in dic.keys():
            if dic[B[i]] == 2:
                print('No')
                exit()
            dic[B[i]] = dic[B[i]] + 1
        else:
            dic[B[i]] = 1

print('Yes')
