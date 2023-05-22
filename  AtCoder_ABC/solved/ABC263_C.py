from sys import stdin as std
import itertools

def main():
    input = std.readline
    N,M = map(int,input().split())
    Combination_Set = list(itertools.combinations(range(1,M+1), N))
    for Tuple in Combination_Set :
        print(" ".join(map(str,Tuple)))

if __name__ == '__main__':
    main()