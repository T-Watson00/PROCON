from sys import stdin as std
import numpy as np

def main():
    input = std.readline
    H_A,W_A = map(int,input().split())
    A = np.array([list(map(int,input().split())) for _ in range(H_A)])
    H_B,W_B = map(int,input().split())
    B = np.array([list(map(int,input().split())) for _ in range(H_B)])
    for h_b in range(H_A)
if __name__ == '__main__':
    main()