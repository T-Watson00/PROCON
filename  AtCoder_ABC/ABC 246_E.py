from sys import stdin as std

def main():
    input = std.readline
    N = int(input())
    n = tuple(range(N))
    A = tuple(map(int,input().split()))
    B = tuple(map(int,input().split()))
    S = list(list(input()) for _ in n)
    S[A[0]][A[1]] = 0
    count = 0
    for i in n:
        if i == 0:
            continue
        else:
            if S[A[0]+i][A[1]+i] == "." :
                try :
                    S[A[0]+i][A[1]+i] = 1

if __name__ == '__main__':
    main()