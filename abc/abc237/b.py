if __name__ == '__main__':
    H, W = map(int, input().split())
    A = [[0 for _ in range(W)] for _ in range(H)]
    A = [[] for _ in range(H)]

    for i in range(H):
        A[i] = list(map(int, input().split()))
    for i in range(W):
        for j in range(H):
            print('{} '.format(A[j][i]), end='')
        print('')
