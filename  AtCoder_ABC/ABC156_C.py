from sys import stdin as std
import numpy as np

def main():
    input = std.readline
    N = int(input())
    X = np.array(list(map(int,input().split())))
    sum_x = np.sum(X)
    sum_x_sec = np.sum(X**2)
    meanx = np.round(sum_x/N)
    sigma = int(sum_x_sec - (2*meanx*sum_x) + (meanx**2)*N)
    print(sigma)

if __name__ == '__main__':
    main()