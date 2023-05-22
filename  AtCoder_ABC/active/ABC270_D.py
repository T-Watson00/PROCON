from sys import stdin as std
from collections import deque



def main():
    input = std.readline
    N,K = map(int,input().split())
    A = deque(map(int,input().split()))
    lest = N
    takahashi = 0
    aoki = 0
    player = "takahashi"
    while lest>0 :
        if A[-1] <= lest :
            lest -= A[-1]
            if player == "takahashi" :
                takahashi += A[-1]
                player = "aoki"
                continue
            elif player == "aoki" :
                aoki += A[-1]
                player = "takahashi"
                continue
        else :
            A.pop()
    print(takahashi)


if __name__ == '__main__':
    main()