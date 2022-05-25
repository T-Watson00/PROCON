from sys import stdin as std
import numpy as np
def main():
    input = std.readline
    N = int(input())
    A = tuple(map(int,input().split()))
    count = 0
    for i in range(N-1) :
        for j in range(i+1,N) :
            count += A.count(A[i]/A[j])
            if A[j] == 1 :
                count -= 1
            count += A.count(A[j]/A[i])
            if A[i] == 1 :
                count -= 1
    print(count)

if __name__ == '__main__':
    main()