if __name__ == '__main__':
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q + 1):
        for j in range(R, S + 1):
            if (- A + i == B - j):
                print('#', end='')
            elif A - i == B - j:
                print('#', end='')
            else:
                print('.', end='')
        print()
