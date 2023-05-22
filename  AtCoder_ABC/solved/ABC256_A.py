from sys import stdin as std
import numpy as np


def main():
    input = std.readline
    N = int(input())
    print(np.power(2,N))


if __name__ == '__main__':
    main()