if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [0 for _ in range(M)]
    B = [0 for _ in range(M)]
    for i in range(M):
        A[i], B[i] = map(int, input().split())
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
print(dic)
