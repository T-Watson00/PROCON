from sys import stdin as std


def main():
    input = std.readline
    L,R = map(int,input().split())
    String = "atcoder"
    print(String[L-1:R])


if __name__ == '__main__':
    main()