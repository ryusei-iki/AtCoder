from collections import deque


if __name__ == '__main__':
    n = int(input())
    s = list(input())
    que = deque()
    que.append(n)

    for i in range(len(s)):
        if (s[len(s) - i -1] == 'R'):
            que.appendleft(len(s) - i - 1)
        else:
            que.append(len(s) - i - 1)
    print(*que)
