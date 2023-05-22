from sys import stdin as std

def main():
    input = std.readline
    moduler = 998244353
    N = int(input())
    surplus = N % moduler
    print(surplus)


if __name__ == '__main__':
    main()