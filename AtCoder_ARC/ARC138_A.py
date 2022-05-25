from sys import stdin as std

def main():
    input = std.readline
    N,K = map(int,input().split())
    A = tuple(map(int,input().split()))
    k = tuple(range(K))
    a = N-1
    if min(A[0:K]) >= max(A[K:]):
        print(-1)
        exit()
    for i in k :
        for j in range(K,a+i):
            if A[i] < A[j] :
                a = min(j - i,a)
                break
    print(a)


if __name__ == '__main__':
    main()