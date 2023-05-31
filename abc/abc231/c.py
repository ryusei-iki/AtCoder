if __name__ == '__main__':
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    x = [0 for _ in range(Q)]
    for i in range(Q):
        x[i] = int(input())
    A_sort = sorted(A, reverse=True)
    num = [7, 5, 1, 6, 9]
    indices = [*range(Q)]
    sorted_indices = sorted(indices, key=lambda i: -x[i])
    sorted_x = [x[i] for i in sorted_indices]
    ans = [0 for i in range(Q)]
    last_n = 0
    step = 0
    for q in range(Q):
        for n in range(last_n, N):
            if A_sort[n] < sorted_x[q]:
                ans[sorted_indices[q]] = n
                last_n = n
                step = 0
                break
            elif n == N - 1:
                ans[sorted_indices[q]] = N

    for i in ans:
        print(i)
