if __name__ == '__main__':
    N = int(input())
    S = dict()
    for i in range(N):
        name = input()
        if name in S.keys():
            S[name] = S[name] + 1
        else:
            S[name] = 1
    max_num = 0
    for i in S.keys():
        if max_num < S[i]:
            max_num = S[i]
            ans = i
    print(ans)
