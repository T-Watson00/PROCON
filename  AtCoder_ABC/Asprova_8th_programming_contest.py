from sys import stdin as std

def main():
    input = std.readline
    S,C,H,a,b = map(int,input().split())
    s = tuple(range(S))
    c = tuple(range(C))
    N = tuple(tuple(map(int,input().split()) for i in s))
    K = tuple(map(int,input().split()))
    A = tuple(tuple(map(int,input().split()) for i in s))
    B = tuple(tuple(map(int,input().split()) for i in c))
    


if __name__ == '__main__':
    main()