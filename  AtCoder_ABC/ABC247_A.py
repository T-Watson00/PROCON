from sys import stdin as std

def main():
    input = std.readline
    S = str(input())
    ans = "0" + S[0:3]
    print(ans)


if __name__ == '__main__':
    main()