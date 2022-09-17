n=int(input())
a=list(map(int,input().split()))

indices = [*range(len(a))]
sorted_indices = sorted(indices, key=lambda i: a[i])

print(sorted_indices[-2]+1)
