from sys import stdin as std

def main():
    input = std.readline
    N = int(input())
    n = tuple(range(1,N))
    A = tuple(map(int,input().split()))
    count = 0
    for i in n:
        if A[i-1] < A[i]:
            count += 1
    print(count)


if __name__ == '__main__':
    main()