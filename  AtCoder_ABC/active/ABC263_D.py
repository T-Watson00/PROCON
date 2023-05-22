from sys import stdin as std
import numpy as np
from collections import deque

def main():
    input = std.readline
    N = input()
    A = list(map(int,input().split()))
    answer = 0
    index_and_element_is_same = 0
    for index in range(N) :
        if index+1 == A[index] :
            index_and_element_is_same += 1
        else :
            if index+1 == A[A[index]-1] :
                



    answer += index_and_element_is_same*(index_and_element_is_same-1)/2


if __name__ == '__main__':
    main()