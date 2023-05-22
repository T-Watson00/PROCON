from sys import stdin as std

def main():
    input = std.readline
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A_all_sorted = sorted(A)
    while True :
        A_initial = A
        for i in range(N-K):
            if A[i] > A[i+K]:
                A[i],A[i+K] = A[i+K],A[i]
        if A_initial == A :
            break
    if A_all_sorted == A :
        print("Yes")
    else :
        print("No")

if __name__ == '__main__':
    main()