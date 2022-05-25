from sys import stdin as std

def main():
    input = std.readline
    N = int(input())
    A = int(len(set(map(int,input().split()))))
    print(A)


if __name__ == '__main__':
    main()