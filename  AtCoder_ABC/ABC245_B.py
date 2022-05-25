from sys import stdin as std

def main():
    input = std.readline
    N = int(input())
    A = set(map(int,input().split()))
    B = set(range(0,2001))
    C = tuple(sorted(B-A))
    print(C[0])

if __name__ == '__main__':
    main()