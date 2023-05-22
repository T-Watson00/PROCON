from sys import stdin as std
import numpy as np


def main():
    input = std.readline
    N = int(input())
    answer = 0
    result = np.array([1,2,3,4,5,6])
    for _ in range(N):
        answer = (sum(result[result > answer])+answer*len(result[result <= answer]))/6
    print(answer)


if __name__ == '__main__':
    main()