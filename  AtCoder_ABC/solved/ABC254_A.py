from sys import stdin as std

def main():
    input = std.readline
    N = str(input())
    print(N[-3:-1])


if __name__ == '__main__':
    main()