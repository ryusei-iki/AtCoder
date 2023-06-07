if __name__ == '__main__':
    s = list(input())
    a_mae = 0
    for i in range(len(s)):
        if (s[i] == 'a'):
            a_mae += 1
            pass
        else:
            break
    a_count = 0
    for i in range(len(s)):
        if (s[len(s) - i - 1] == 'a'):
            a_count += 1
            pass
        else:
            last = len(s) - i
            break
    if (a_mae <= a_count):
        pass
    else:
        print('No')
        exit()
    if (a_mae == len(s)):
        print('Yes')
        exit()

    for i in range(a_mae, (last - a_mae) // 2 + a_mae):
        if (s[i] == s[len(s) - a_count - (i - a_mae) - 1]):
            pass
        else:
            print('No')
            exit()
    print('Yes')
