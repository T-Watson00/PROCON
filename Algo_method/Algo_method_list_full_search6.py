from sys import stdin as std

def main():
    input = std.readline
    N = int(input())
    A = set(map(int,input().split()))
    print(max(A))


if __name__ == '__main__':
    main()