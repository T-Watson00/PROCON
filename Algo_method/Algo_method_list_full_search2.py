from sys import stdin as std

def main():
    input = std.readline
    N,V = map(int,input().split())
    A = tuple(map(int,input().split()))
    Count = A.count(V)
    print(Count)
if __name__ == '__main__':
    main()