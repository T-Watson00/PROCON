from sys import stdin as std
import numpy as np

def main():
    input = std.readline
    N = int(input())
    NN_list = np.array([np.power(n,2) for n in range(1,N+1)])
    count = 0
    for i in range(1,N+1):
        count += np.count_nonzero((NN_list <= i*N) & (NN_list % i == 0))
    print(count)

if __name__ == '__main__':
    main()