from sys import stdin as std
import numpy as np


def main():
    input = std.readline
    N,X,Y = map(int,input().split())
    node_list = np.array(sorted([tuple(sorted([map(int,input.split())])) for _ in range(N-1)]))
    edge_set = np.array([[i,0] for i in range(1,N+1) ])
    edge_set[0][1] = 0
    Depth = [1]
    count = 1
    while count < N :
        for depth in Depth :
            new_depth = [np.where(node_list[:,0])]
            count += new_depth.size()


if __name__ == '__main__':
    main()