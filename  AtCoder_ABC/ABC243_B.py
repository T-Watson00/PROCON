from sys import stdin as std

def main():
    input = std.readline
    N = int(input())
    n = tuple(range(N))
    A = tuple(map(int,input().split()))
    B = tuple(map(int,input().split()))
    Hit = 0
    Brow = len(set(set(A) & set(B)))
    for i in n :
        if A[i] == B[i] :
            Hit += 1
    Brow = Brow - Hit
    print(Hit)
    print(Brow)

if __name__ == '__main__':
    main()