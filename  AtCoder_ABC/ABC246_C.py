from sys import stdin as std

def main():
    input = std.readline
    N,K,X = map(int,input().split())
    A = list(map(int,input().split()))
    n = tuple(range(N))
    count = 0
    result = sum(A)
    for i in n :
        count += (A[i] // X)
        A[i] = A[i] % X
    if count >= K :
        result -= K*X
    elif count < K :
        A = sorted(A,reverse=True)
        m = K-count
        result -= (sum(A[0:m])+count*X)
    print(result)

if __name__ == '__main__':
    main()
