if __name__ == '__main__':
    s = input()
    count = [0 for i in range(2)]
    for i in range(len(s)):
        if i == 0:
            pass
        elif i == 1:
            if s[i] == 'o' and s[i - 1] == 'x':
                pass
            elif s[i] == 'x':
                pass
            else:
                print('No')
                exit()
        elif 2 <= i:
            if s[i] == 'o' and (s[i - 1] == 'x' and s[i - 2] == 'x'):
                pass
            elif s[i] == 'x' and (s[i - 1] == 'x' and s[i - 2] == 'o'):
                pass
            elif s[i] == 'x' and (s[i - 1] == 'o' and s[i - 2] == 'x'):
                pass
            else:
                print('No')
                exit()
    print('Yes')
