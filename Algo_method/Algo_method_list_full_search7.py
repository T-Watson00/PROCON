from sys import stdin as std

def main():
    input = std.readline
    N = int(input())
    n = tuple(range(1,N))
    A = tuple(map(int,input().split()))
    max = (A[0],0)
    for i in n:
        if max[0] < A[i]:
            max = (A[i],i)
    print(max[1])


if __name__ == '__main__':
    main()