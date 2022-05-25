from sys import stdin as std
import numpy as np

def main():
    input = std.readline
    N,M,C = map(int,input().split())
    n = tuple(range(N))
    C = np.array([C]*N).reshape((N,1))
    B = np.array(tuple(map(int,input().split()))).reshape((M,1))
    A = np.array(tuple(np.array(tuple(map(int,input().split()))) for _ in n ))
    X = (A@B) + C
    result = np.count_nonzero(X > 0)
    print(result)

if __name__ == '__main__':
    main()