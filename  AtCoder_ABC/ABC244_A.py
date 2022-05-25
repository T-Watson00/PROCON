from sys import stdin as std

def main():
    input = std.readline
    N = int(input())
    S = tuple(input())
    print(S[N-1])

if __name__ == '__main__':
    main()